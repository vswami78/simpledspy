from typing import Dict, List, Any
import dspy
from .module_factory import ModuleFactory
from .pipeline_manager import PipelineManager

class PipeFunction:
    _instances: Dict[str, 'PipeFunction'] = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

    def __init__(self):
        self.pipeline_manager = PipelineManager()
        self.module_factory = ModuleFactory()

    def _create_module(self, inputs: List[str], outputs: List[str], description: str = "") -> dspy.Module:
        return self.module_factory.create_module(inputs, outputs, description)

    def _get_assignment_target(self) -> str:
        import inspect
        frame = inspect.currentframe().f_back.f_back
        code_context = frame.f_code.co_filename
        if code_context == '<string>':
            return 'result'
        return frame.f_locals.get('__pipe_target', 'result')

    def __call__(self, *args, **kwargs):
        inputs = [arg for arg in args]
        outputs = [self._get_assignment_target()]
        
        module = self._create_module(
            inputs=[str(type(arg)) for arg in args],
            outputs=outputs
        )
        
        self.pipeline_manager.register_step(
            inputs=inputs,
            outputs=outputs,
            module=module
        )
        
        result = module(*args, **kwargs)
        if isinstance(result, dict):
            return next(iter(result.values()))
        return result

pipe = PipeFunction()
