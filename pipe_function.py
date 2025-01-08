from typing import Any, Tuple, List
from pipeline_manager import PipelineManager

class PipeFunction:
    def __init__(self):
        self.pipeline_manager = PipelineManager()

    def __call__(self, *args, outputs: List[str], modules: List[Any]) -> Tuple[Any, ...]:
        """
        Executes modules immediately and registers the steps.
        
        Args:
            *args: Input arguments
            outputs: List of output field names
            modules: List of DSPy modules to process the inputs
            
        Returns:
            Tuple containing the outputs
        """
        if not outputs or not modules:
            raise ValueError("Both outputs and modules parameters are required")
        if len(outputs) != len(modules):
            raise ValueError("Number of outputs must match number of modules")
            
        # Execute modules and collect results
        results = [module(*args) for module in modules]
        
        # Register steps using actual input names from module signatures
        for module, output in zip(modules, outputs):
            inputs = list(module.signature.input_fields.keys())
            self.pipeline_manager.register_step(inputs=inputs, outputs=[output], module=module)
            
        return tuple(results)

# Instantiate the pipe function
pipe = PipeFunction()
