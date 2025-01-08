from simpledspy import pipe
from simpledspy import PipelineManager

if __name__ == "__main__":
    # Test basic functionality
    result = pipe("abc def ghi jkl")
    print(result)  # Should print: {'result': 'abc def ghi jkl'}
    
    # Assemble and run pipeline
    pipeline_manager = PipelineManager()
    assembled_pipeline = pipeline_manager.assemble_pipeline()
    pipeline_result = assembled_pipeline("input data")
    print(pipeline_result)
