from pipe_function import pipe
from pipeline_manager import PipelineManager
from metrics import exact_match_metric
from dspy.teleprompt import MIPROv2
from typing import List, Dict, Any, Tuple

def run_pipeline(inputs: List[Dict[str, Any]], modules: List[Any], outputs: List[str]) -> List[Tuple[Any, ...]]:
    """
    Generic function to run a DSPy pipeline.
    
    Args:
        inputs: List of input dictionaries
        modules: List of DSPy modules to process the inputs
        outputs: List of output field names
        
    Returns:
        List of tuples containing the outputs for each input
    """
    results = []
    for input_data in inputs:
        result = pipe(
            *input_data.values(),
            outputs=outputs,
            modules=modules
        )
        results.append(result)
    return results

if __name__ == "__main__":
    # Example usage
    pipeline_manager = PipelineManager()
    
    # Initialize optimizer
    optimizer = MIPROv2(
        metric=exact_match_metric,
        auto="light",
        num_threads=24
    )
    
    # Example pipeline execution
    try:
        assembled_pipeline = pipeline_manager.assemble_pipeline()
        print("Pipeline assembled successfully")
    except ValueError as e:
        print(f"Pipeline assembly error: {e}")
