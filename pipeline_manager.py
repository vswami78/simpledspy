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

    def assemble_pipeline(self) -> dspy.ChainOfThought:
        """
        Assembles the registered steps into a single DSPy ChainOfThought module.
        
        Returns:
            dspy.ChainOfThought: The assembled DSPy pipeline.
        """
        if not self.pipeline_steps:
            raise ValueError("No pipeline steps registered. Please make pipe calls before assembling the pipeline.")
        
        # Collect all unique input and output field names
        all_inputs = set()
        all_outputs = set()
        for step in self.pipeline_steps:
            all_inputs.update(step['inputs'])
            all_outputs.update(step['outputs'])
        
        signature_fields = {}
        for inp in all_inputs:
            signature_fields[inp] = dspy.InputField(desc=f"Input field {inp}.")
        for outp in all_outputs:
            signature_fields[outp] = dspy.OutputField(desc=f"Output field {outp}.")

        # Dynamically create the Signature class
        DynamicSignature = type(
            'DynamicSignature',
            (dspy.Signature,),
            signature_fields
        )

        # Initialize the ChainOfThought with the dynamic signature
        program = dspy.ChainOfThought(DynamicSignature)

        # Add all registered modules to the ChainOfThought
        for step in self.pipeline_steps:
            program.add_module(step['module'])
        
        print("Assembled the DSPy pipeline with all registered steps.")
        return program
