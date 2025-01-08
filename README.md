# DSPy Pipeline

A simple system for building and running DSPy pipelines.

## Architecture

1. **ModuleFactory**: Creates DSPy modules from input/output specifications
2. **PipelineManager**: Manages pipeline steps and assembly
3. **PipeFunction**: Handles immediate execution and optimization routing
4. **Metrics**: Provides evaluation metrics

## Quick Start

```python
# Create pipeline
inputs = ["text", "cv"]
outputs = ["name", "degree_bool", "age"]
modules = [
    module_factory.create_module(inputs, ["name"]),
    module_factory.create_module(inputs, ["degree_bool"]),
    module_factory.create_module(inputs, ["age"])
]

# Run pipeline
results = pipe(application_mail_text, application_cv, outputs=outputs, modules=modules)
```

## TODO

1. Add input validation
2. Add error handling
3. Add documentation
4. Add example test cases

