# DSPy Pipeline System

A generic pipeline system for building and optimizing DSPy workflows.

## Key Features

- Generic pipeline execution with `run_pipeline()`
- Pipeline step registration and management
- Automatic pipeline optimization
- Extensible architecture for custom modules
- Input/output validation
- Caching and optimization support

## Core Components

1. **Pipeline Manager**  
   Manages pipeline steps and assembles the final pipeline

2. **Pipe Function**  
   Handles immediate execution and optimization routing

3. **Metrics**  
   Provides evaluation metrics for pipeline optimization

4. **Pipeline Execution**  
   Generic pipeline runner for processing inputs

## Usage

```python
from main import run_pipeline
from pipeline_manager import PipelineManager
from metrics import exact_match_metric
from dspy.teleprompt import MIPROv2

# Define your custom modules
class MyModule1:
    def __call__(self, input):
        return process(input)

class MyModule2:
    def __call__(self, input):
        return process(input)

# Create pipeline inputs
inputs = [
    {"input1": "data1", "input2": "data2"},
    {"input1": "data3", "input2": "data4"}
]

# Define modules and outputs
modules = [MyModule1(), MyModule2()]
outputs = ["output1", "output2"]

# Run pipeline
results = run_pipeline(inputs, modules, outputs)

# Optimize pipeline
pipeline_manager = PipelineManager()
optimizer = MIPROv2(metric=exact_match_metric)
optimized_pipeline = optimizer.compile(
    pipeline_manager.assemble_pipeline(),
    trainset=training_data
)
```

## Development

1. Create custom modules implementing `__call__`
2. Register pipeline steps through `pipe()` calls
3. Assemble and optimize pipeline
4. Execute with `run_pipeline()`

## Requirements

- Python 3.8+
- DSPy
- Typing extensions

## Installation

```bash
pip install -r requirements.txt
```

## Contributing

1. Fork the repository
2. Create feature branch
3. Submit pull request

## License

MIT License
