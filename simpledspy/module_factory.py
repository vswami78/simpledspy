import dspy
from typing import List, Dict, Any

class ModuleFactory:
    def create_module(self, inputs: List[str], outputs: List[str], description: str = "") -> dspy.Module:
        """
        Creates a DSPy module with specified inputs and outputs.
        
        Args:
            inputs: List of input field names
            outputs: List of output field names
            description: Optional description of the module's purpose
            
        Returns:
            dspy.Module: Configured DSPy module
        """
        # Create signature fields with proper prefixes
        # signature_fields = {}
        # for i, inp in enumerate(inputs):
            # # Use the actual variable name if available, otherwise generic input_X
            # field_name = inp if not inp.startswith('input_') else f"input_{i+1}"
            # signature_fields[field_name] = dspy.InputField(
                # prefix=f"{field_name.capitalize()}:",
                # desc=f"Input field {field_name}"
            # )
        # # Create separate output fields for each output
        # print("outputs:", outputs)
        # for i, outp in enumerate(outputs):
            # field_name = f"output_{i+1}" if len(outputs) > 1 else outp
            # signature_fields[field_name] = dspy.OutputField(
                # prefix=f"{outp.capitalize()}:",
                # desc=f"Output field {outp}"
            # )


        signature_fields = {}
        for inp in inputs:
            signature_fields[inp] = dspy.InputField(desc=f"Input field {inp}")
        for outp in outputs:
            signature_fields[outp] = dspy.OutputField(desc=f"Output field {outp}")




        # Create signature class with proper instructions
        instructions = description or f"Given the fields {', '.join(inputs)}, produce the fields {', '.join(outputs)}."
        Signature = type(
            'Signature',
            (dspy.Signature,),
            {
                '__doc__': instructions,
                **signature_fields
            }
        )

        # Create and return Predict module
        # print("Signature:", Signature)
        return dspy.Predict(Signature)
