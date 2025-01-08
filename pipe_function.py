from typing import Any, Tuple, List
import dspy
from pipeline_manager import PipelineManager
from module_factory import ModuleFactory

class PipeFunction:
    def __init__(self):
        self.pipeline_manager = PipelineManager()
        self.module_factory = ModuleFactory()
        # Configure default LM
        self.lm = dspy.LM(model="deepseek/deepseek-chat")
        dspy.configure(lm=self.lm)

    def _create_module(self, inputs: List[str], outputs: List[str], description: str = "") -> dspy.Module:
        """Create a DSPy module with the given signature."""
        return self.module_factory.create_module(
            inputs=inputs,
            outputs=outputs,
            description=description
        )

    def __call__(self, *args, inputs: List[str], outputs: List[str], description: str = "") -> Tuple[Any, ...]:
        """
        Executes a DSPy module with the given signature.
        
        Args:
            *args: Input arguments
            inputs: List of input field names
            outputs: List of output field names
            description: Description of the module's purpose
            
        Returns:
            Tuple containing the outputs
        """
        if len(inputs) != len(args):
            raise ValueError(f"Expected {len(inputs)} inputs but got {len(args)}")
            
        # Create module dynamically
        module = self._create_module(inputs, outputs, description)
        
        # Create input dict
        input_dict = {field: arg for field, arg in zip(inputs, args)}
        
        # Execute module
        result = module(**input_dict)
        
        # Register step
        self.pipeline_manager.register_step(inputs=inputs, outputs=outputs, module=module)
        
        # Return outputs
        return tuple(getattr(result, output) for output in outputs)

# Instantiate the pipe function
pipe = PipeFunction()
