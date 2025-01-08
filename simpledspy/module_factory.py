from typing import List
import dspy

class ModuleFactory:
    def create_module(self, inputs: List[str], outputs: List[str], description: str = "") -> dspy.Module:
        class DynamicModule(dspy.Module):
            def __init__(self):
                super().__init__()
                self.input_fields = inputs
                self.output_fields = outputs

            def forward(self, *args):
                if len(self.output_fields) == 1:
                    return args[0]
                return args

        return DynamicModule()
