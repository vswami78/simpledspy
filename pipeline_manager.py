import os
from typing import Any, List, Dict
import dspy

class PipelineManager:
    """
    Singleton class to manage the DSPy pipeline steps.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PipelineManager, cls).__new__(cls)
            cls._instance.pipeline_steps = []
            cls._instance.cache_dir = "./dspy_pipeline_cache/"
            if not os.path.exists(cls._instance.cache_dir):
                os.makedirs(cls._instance.cache_dir)
        return cls._instance

    def register_step(self, inputs: List[str], outputs: List[str], module: Any):
        """
        Registers a DSPy module with specified inputs and outputs.
        
        Args:
            inputs (List[str]): List of input field names.
            outputs (List[str]): List of output field names.
            module (Any): DSPy module or function to process the inputs.
        """
        step = {
            "inputs": inputs,
            "outputs": outputs,
            "module": module
        }
        self.pipeline_steps.append(step)
        print(f"Registered step: {inputs} -> {outputs}")

    def assemble_pipeline(self) -> dspy.Module:
        """
        Assembles the registered steps into a DSPy pipeline module.
        
        Returns:
            dspy.Module: The assembled DSPy pipeline.
        """
        if not self.pipeline_steps:
            raise ValueError("No pipeline steps registered. Please make pipe calls before assembling the pipeline.")
        
        # Create a simple DSPy module that chains the steps
        class Pipeline(dspy.Module):
            def __init__(self, steps):
                super().__init__()
                self.steps = steps
                for i, step in enumerate(steps):
                    setattr(self, f'step{i}', step['module'])
            
            def forward(self, **inputs):
                results = {}
                for step in self.steps:
                    # Get inputs for this step
                    step_inputs = {k: inputs[k] for k in step['inputs']}
                    # Run the module
                    module = getattr(self, f'step{self.steps.index(step)}')
                    step_output = module(**step_inputs)
                    # Store outputs
                    for output in step['outputs']:
                        results[output] = getattr(step_output, output)
                return results
        
        return Pipeline(self.pipeline_steps)
