# SimpleDSPy

[![PyPI version](https://badge.fury.io/py/simpledspy.svg)](https://badge.fury.io/py/simpledspy)
[![Python Version](https://img.shields.io/pypi/pyversions/simpledspy)](https://pypi.org/project/simpledspy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://github.com/tomdoerr/simpledspy/actions/workflows/tests.yml/badge.svg)](https://github.com/tomdoerr/simpledspy/actions/workflows/tests.yml)

SimpleDSPy is a lightweight Python library that simplifies building and running DSPy pipelines with an intuitive interface.

## Features

- Automatic module creation from input/output names
- Pipeline management and step tracking
- Clean, minimal API
- Built-in caching and configuration
- Type hints and documentation

## Installation

```bash
pip install simpledspy
```

## Quick Start

```python
from simpledspy import pipe

# Basic text processing
cleaned_text = pipe("Some messy   text with extra spaces")
print(cleaned_text)  # "Some messy text with extra spaces"

# Multiple inputs/outputs
name, age = pipe("John Doe, 30 years old")
print(name)  # "John Doe"
print(age)   # 30

# Custom descriptions
full_name = pipe(
    "John", "Doe", 
    description="Combine first and last names"
)
print(full_name)  # "John Doe"
```

## How It Works

The `pipe` function automatically:
1. Detects input variable names
2. Creates appropriate DSPy modules
3. Tracks pipeline steps
4. Returns processed outputs

## Advanced Usage

### Pipeline Management

```python
from simpledspy import PipelineManager

# Get pipeline steps
manager = PipelineManager()
pipeline = manager.assemble_pipeline()

# Run entire pipeline
result = pipeline("input1", "input2")
```

### Custom Modules

```python
from simpledspy import ModuleFactory

# Create custom module
factory = ModuleFactory()
module = factory.create_module(
    inputs=["text"],
    outputs=["cleaned_text"],
    description="Clean and normalize text"
)

# Use module
cleaned = module(" Some text ")
print(cleaned.cleaned_text)  # "Some text"
```

## Configuration

Configure the language model and caching:

```python
import dspy
from simpledspy import pipe

# Custom LM configuration
pipe.lm = dspy.LM(model="gpt-4")
dspy.configure(lm=pipe.lm, cache=True)
```

## Contributing

Contributions are welcome! Please open an issue or pull request on GitHub.

## License

MIT License

