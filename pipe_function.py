from typing import Any, Tuple, List, Callable
import dspy
from pipeline_manager import PipelineManager
from module_factory import ModuleFactory
import inspect

class PipeFunction:
    def __init__(self):
        self.pipeline_manager = PipelineManager()
        self.module_factory = ModuleFactory()
        # Configure default LM with caching disabled
        self.lm = dspy.LM(model="deepseek/deepseek-chat")
        dspy.configure(lm=self.lm, cache=False)

    def _create_module(self, inputs: List[str], outputs: List[str], description: str = "") -> dspy.Module:
        """Create a DSPy module with the given signature."""
        return self.module_factory.create_module(
            inputs=inputs,
            outputs=outputs,
            description=description
        )

    def _get_assignment_target(self) -> str:
        """Get the name of the variable being assigned to."""
        frame = inspect.currentframe()
        try:
            # Go up two frames to get the assignment context
            outer_frame = frame.f_back.f_back
            code_context = outer_frame.f_code.co_code
            names = outer_frame.f_code.co_names
            # Look for STORE_NAME opcode (90)
            for i in range(len(code_context)):
                if code_context[i] == 90:  # STORE_NAME opcode
                    return names[code_context[i+1]]
        finally:
            del frame
        return "output"

    def __call__(self, *args, description: str = None) -> Any:
        """
        Executes a DSPy module with the given signature.
        
        Args:
            *args: Input arguments
            description: Optional description of the module's purpose
            
        Returns:
            The output value
        """
        # Get the assignment target name
        output_name = self._get_assignment_target()
        
        # Infer input names from args
        inputs = [f"input_{i+1}" for i in range(len(args))]
        
        # Generate default description if none provided
        if description is None:
            input_types = [type(arg).__name__ for arg in args]
            description = f"Processes {len(args)} inputs of types: {', '.join(input_types)}"
            
        # Create module dynamically
        module = self._create_module(inputs, [output_name], description)
        
        # Create input dict
        input_dict = {field: arg for field, arg in zip(inputs, args)}
        
        # Execute module
        result = module(**input_dict)
        
        # Register step
        self.pipeline_manager.register_step(inputs=inputs, outputs=[output_name], module=module)
        
        # Return the output value
        return getattr(result, output_name)

# Instantiate the pipe function
pipe = PipeFunction()
