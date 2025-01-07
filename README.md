# DSPy Pipeline

A simple system for building and running DSPy pipelines.

## Quick Start

```python
from main import run_pipeline
from pipeline_manager import PipelineManager

# Create pipeline
inputs = [{"input1": "data1", "input2": "data2"}]
modules = [MyModule1(), MyModule2()]
outputs = ["output1", "output2"]

# Run pipeline
results = run_pipeline(inputs, modules, outputs)
```

## Installation

```bash
pip install -r requirements.txt
```

## License

MIT
