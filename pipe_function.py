from typing import Any, Tuple, List, Dict
from pipeline_manager import PipelineManager
from module_factory import ModuleFactory

class PipeFunction:
    def __init__(self):
        self.pipeline_manager = PipelineManager()
        self.module_factory = ModuleFactory()
        self.optimized = False

    def optimize(self, optimized_pipeline: Any):
        """
        Sets the pipeline as optimized and stores the optimized pipeline.
        
        Args:
            optimized_pipeline (Any): The optimized DSPy pipeline module.
        """
        self.optimized = True
        self.optimized_pipeline = optimized_pipeline

    def __call__(self, *args, outputs: List[str] = None, modules: List[Any] = None) -> Tuple[Any, ...]:
        """
        Acts as the pipe interface. Executes modules immediately and registers the steps.
        If the pipeline is optimized, routes the call to the optimized pipeline.
        
        Args:
            *args: Input arguments corresponding to the DSPy inputs.
            outputs (List[str], optional): List of output field names.
            modules (List[Any], optional): List of DSPy modules or functions to process the inputs.
        
        Returns:
            Tuple[Any, ...]: A tuple containing the outputs in the order specified.
        """
        if self.optimized:
            # Execute via the optimized pipeline
            input_field_names = [f"input{i+1}" for i in range(len(args))]
            input_dict = {f"{name}": arg for name, arg in zip(input_field_names, args)}
            return tuple(getattr(self.optimized_pipeline(**input_dict), outp, None) for outp in input_field_names)
        
        # Before optimization: Execute modules immediately and register steps
        if outputs is None:
            raise ValueError("You must specify the 'outputs' parameter as a list of output field names.")
        if modules is None:
            raise ValueError("You must provide DSPy modules via the 'modules' parameter.")
        if len(outputs) != len(modules):
            raise ValueError("The number of outputs must match the number of modules provided.")
        if len(args) < 1:
            raise ValueError("At least one input argument is required.")
        
        # Define input field names based on the number of inputs
        input_field_names = [f"input{i+1}" for i in range(len(args))]
        
        # Execute each module and collect the results
        results = []
        for module in modules:
            result = module(*args)
            results.append(result)
        
        # Register each step with the PipelineManager
        for output, module in zip(outputs, modules):
            self.pipeline_manager.register_step(inputs=input_field_names, outputs=[output], module=module)
        
        return tuple(results)

# Instantiate the pipe function
pipe = PipeFunction()
