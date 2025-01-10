from typing import Any, Tuple, List, Callable, Dict
import dspy
from .pipeline_manager import PipelineManager
from .module_factory import ModuleFactory
import inspect
import os
import dis

class PipeFunction:
    _instances: Dict[str, 'PipeFunction'] = {}

    def __new__(cls, *args, **kwargs):
        # Get the caller's file and line number
        frame = inspect.currentframe().f_back
        location = f"{os.path.basename(frame.f_code.co_filename)}:{frame.f_lineno}"
        
        # Create or return existing instance for this location
        if location not in cls._instances:
            instance = super(PipeFunction, cls).__new__(cls)
            cls._instances[location] = instance
            instance._initialized = False
            instance._location = location
        return cls._instances[location]

    def __init__(self):
        if getattr(self, '_initialized', False):
            return
        self._initialized = True
        self.pipeline_manager = PipelineManager()
        self.module_factory = ModuleFactory()
        # Configure default LM with caching disabled
        self.lm = dspy.LM(model="deepseek/deepseek-chat")
        dspy.configure(lm=self.lm, cache=False)
        # print(f"Initialized new PipeFunction at {self._location}")

    def _create_module(self, inputs: List[str], outputs: List[str], description: str = "") -> dspy.Module:
        """Create a DSPy module with the given signature."""
        return self.module_factory.create_module(
            inputs=inputs,
            outputs=outputs,
            description=description
        )

    def _get_caller_context(self, num_args: int) -> Tuple[List[str], str]:
        """Get the names of variables being passed and assigned.
        
        Args:
            num_args: Number of arguments expected
        """
        frame = inspect.currentframe()
        try:
            # Go up two frames to get the assignment context
            outer_frame = frame.f_back.f_back
            # Get the bytecode for the current frame
            bytecode = dis.Bytecode(outer_frame.f_code)
            
            # Find the variable names being passed
            input_names = []
            seen_ops = set()
            
            # Walk backwards through instructions to find actual inputs
            for instr in reversed(list(bytecode)):
                if instr.offset >= outer_frame.f_lasti:
                    continue
                    
                # Skip if we've already seen this operation
                if instr.offset in seen_ops:
                    continue
                seen_ops.add(instr.offset)
                
                # Only include LOAD operations that are actual inputs
                if instr.opname in ('LOAD_NAME', 'LOAD_FAST'):
                    # Skip function names and other non-inputs
                    if instr.argval not in ('pipe', 'print', 'self'):
                        # Only add if it's one of our actual arguments
                        if len(input_names) < num_args:
                            input_names.append(instr.argval)
            
            # Reverse to maintain original order and ensure correct count
            input_names = list(reversed(input_names))
            
            # If we didn't get enough names, fill with generic ones
            if len(input_names) < num_args:
                input_names.extend(f"input_{i+1}" for i in range(len(input_names), num_args))
                
            # Find the STORE_NAME/STORE_FAST opcode that follows our call
            output_name = None
            for instr in bytecode:
                if instr.offset > outer_frame.f_lasti:
                    if instr.opname in ('STORE_NAME', 'STORE_FAST'):
                        output_name = instr.argval
                        break
            
            if not output_name:
                raise ValueError("pipe must be called in an assignment context.")
            
            # Remove duplicates and the output name from inputs
            input_names = list(dict.fromkeys(input_names))
            if output_name in input_names:
                input_names.remove(output_name)
            
            return input_names, output_name
        finally:
            del frame

    def __call__(self, *args, description: str = None) -> Any:
        """
        Executes a DSPy module with the given signature.
        
        Args:
            *args: Input arguments
            description: Optional description of the module's purpose
            
        Returns:
            The output value
        """
        # Get the input and output variable names
        input_names, output_name = self._get_caller_context(len(args))
        print("input_names:", input_names)
        
        # Use actual input names if we found them, otherwise fall back to generic names
        if len(input_names) != len(args):
            input_names = [f"input_{i+1}" for i in range(len(args))]
            
        # Create module dynamically with correct output names
        # If output_name contains multiple names separated by commas, split them
        output_names = [name.strip() for name in output_name.split(',')]
        module = self._create_module(input_names, output_names, description)
        
        # Create input dict
        input_dict = {field: arg for field, arg in zip(input_names, args)}
        
        # Execute module
        result = module(**input_dict)
        
        # Register step
        self.pipeline_manager.register_step(inputs=input_names, outputs=output_names, module=module)
        
        # Handle outputs based on the output_names list
        if len(output_names) == 1:
            return getattr(result, output_names[0])
        else:
            return tuple(getattr(result, field) for field in output_names)

# Instantiate the pipe function
pipe = PipeFunction()
