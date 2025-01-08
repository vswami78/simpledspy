import pytest
from module_factory import ModuleFactory
from pipeline_manager import PipelineManager

def test_module_creation():
    """Test module creation with inputs and outputs"""
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
