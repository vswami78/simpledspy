from typing import Any, Tuple, List
from pipeline_manager import PipelineManager

class PipeFunction:
    def __init__(self):
        self.pipeline_manager = PipelineManager()

    def __call__(self, *args, modules: List[Any]) -> Tuple[Any, ...]:
        """
        Executes modules immediately and registers the steps.
        
        Args:
            *args: Input arguments
            modules: List of DSPy modules to process the inputs
            
        Returns:
            Tuple containing the outputs
        """
        if not modules:
            raise ValueError("Modules parameter is required")
            
        # Get outputs from module signatures
        outputs = []
        for module in modules:
            outputs.extend(list(module.signature.output_fields.keys()))
            
        # Execute modules and collect results
        results = [module(*args) for module in modules]
        
        # Register steps using actual input/output names from module signatures
        for module in modules:
            inputs = list(module.signature.input_fields.keys())
            module_outputs = list(module.signature.output_fields.keys())
            self.pipeline_manager.register_step(inputs=inputs, outputs=module_outputs, module=module)
            
        return tuple(results)

# Instantiate the pipe function
pipe = PipeFunction()
