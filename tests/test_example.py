import pytest
from simpledspy import pipe

def test_second_word_extraction():
    """Test extracting second word from text"""
    list_jkl = "abc def ghi jkl iowe afj wej own iow jklwe"
    list_oqc = "oid iwfo fjs wjiof sfio we x dso weop vskl we"
    
    second_word_list_oqc = pipe(list_jkl, list_oqc)
    assert second_word_list_oqc == "iwfo"

def test_module_creation():
    """Test module creation with inputs and outputs"""
    from module_factory import ModuleFactory
    factory = ModuleFactory()
    module = factory.create_module(
        inputs=["input_text"],
        outputs=["output_length"],
        description="Test module that returns input length"
    )
    
    # Verify module has expected attributes
    assert hasattr(module, 'signature')
    assert hasattr(module, 'forward')
    assert hasattr(module.signature, 'input_text')
    assert hasattr(module.signature, 'output_length')

def test_pipeline_assembly():
    """Test assembling multiple modules into a pipeline"""
    from pipeline_manager import PipelineManager
    from module_factory import ModuleFactory
    
    manager = PipelineManager()
    
    # Register pipeline steps
    manager.register_step(
        inputs=["input_text"],
        outputs=["text_length"],
        module=ModuleFactory().create_module(
            inputs=["input_text"],
            outputs=["text_length"],
            description="Get text length"
        )
    )
    
    manager.register_step(
        inputs=["text_length"],
        outputs=["is_long"],
        module=ModuleFactory().create_module(
            inputs=["text_length"],
            outputs=["is_long"],
            description="Check if text is long"
        )
    )
    
    # Assemble pipeline
    pipeline = manager.assemble_pipeline()
    
    # Verify pipeline structure
    assert len(pipeline.steps) == 2
    assert hasattr(pipeline.steps[0], 'signature')
    assert hasattr(pipeline.steps[1], 'signature')
