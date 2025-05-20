<h1 align="center">SimpleDSPy</h1>

<p align="center">
  <a href="https://pypi.org/project/simpledspy/">
    <img src="https://img.shields.io/static/v1?style=for-the-badge&label=PyPI&message=simpledspy&color=blue" alt="PyPI version">
  </a>
  <a href="https://pypi.org/project/simpledspy/">
    <img src="https://img.shields.io/static/v1?style=for-the-badge&label=Python&message=3.9+%7C+3.10+%7C+3.11&color=blue" alt="Python Version">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/static/v1?style=for-the-badge&label=License&message=MIT&color=blue" alt="License: MIT">
  </a>
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/static/v1?style=for-the-badge&label=Code%20Style&message=Black&color=black" alt="Code style: black">
  </a>
  <a href="https://github.com/tomdoerr/simpledspy/actions/workflows/tests.yml">
    <img src="https://img.shields.io/static/v1?style=for-the-badge&label=Tests&message=Passing&color=green" alt="Tests">
  </a>
</p>

<p align="center">
  SimpleDSPy is a lightweight Python library that simplifies building and running DSPy pipelines with an intuitive interface.
</p>

> **Note:** This project is currently a work in progress and is not officially affiliated with or endorsed by the DSPy project. It is an independent effort to create a simplified interface for working with DSPy pipelines.

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

## Architecture (credit: gitdiagram)

```mermaid
flowchart TD
    %% User
    User["User (Script/CLI)"]:::external

    %% Public Interface
    subgraph "Public Interface"
        API["pipe() API"]:::api
        CLI["CLI (simpledspy/cli.py)"]:::api
    end

    %% Core Library
    subgraph "Core Library"
        Factory["Module Factory"]:::core
        PMgrRoot["Pipeline Manager (root)"]:::core
        PMgrInternal["Pipeline Manager (internal)"]:::core
        OptMgr["Optimization Manager"]:::core
        Metrics["Metrics Collector"]:::core
    end

    %% External Dependency
    ExternalDSPy["External DSPy Library"]:::external

    %% Supporting Artifacts
    subgraph "Supporting Artifacts"
        Tests["Test Suite"]:::external
        Config["pyproject.toml"]:::external
        README["README.md"]:::external
        Plan["plan.md"]:::external
    end

    %% Connections
    User --> API
    User --> CLI
    API --> Factory
    CLI --> PMgrRoot
    PMgrRoot --> PMgrInternal
    Factory --> PMgrInternal
    PMgrInternal --> OptMgr
    OptMgr --> PMgrInternal
    PMgrInternal --> ExternalDSPy
    PMgrInternal --> Metrics
    PMgrInternal --> API
    PMgrInternal --> CLI

    %% Click Events
    click API "https://github.com/vswami78/simpledspy/blob/main/simpledspy/pipe.py"
    click CLI "https://github.com/vswami78/simpledspy/blob/main/simpledspy/cli.py"
    click Factory "https://github.com/vswami78/simpledspy/blob/main/simpledspy/module_factory.py"
    click PMgrInternal "https://github.com/vswami78/simpledspy/blob/main/simpledspy/pipeline_manager.py"
    click PMgrRoot "https://github.com/vswami78/simpledspy/blob/main/pipeline_manager.py"
    click OptMgr "https://github.com/vswami78/simpledspy/blob/main/simpledspy/optimization_manager.py"
    click Metrics "https://github.com/vswami78/simpledspy/blob/main/metrics.py"
    click Tests "https://github.com/vswami78/simpledspy/blob/main/tests/test_example.py"
    click Config "https://github.com/vswami78/simpledspy/blob/main/pyproject.toml"
    click README "https://github.com/vswami78/simpledspy/blob/main/README.md"
    click Plan "https://github.com/vswami78/simpledspy/blob/main/plan.md"

    %% Styles
    classDef api fill:#FF7100,stroke:#333,stroke-width:1px
    classDef core fill:#812FFF,stroke:#333,stroke-width:1px
    classDef external fill:#CA87FA,stroke:#333,stroke-width:1px
```
## Contributing

Contributions are welcome! Please open an issue or pull request on GitHub.

## License

MIT License

