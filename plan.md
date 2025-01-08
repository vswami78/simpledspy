# DSPy Pipeline Code Overview

## Core Components

### 1. ModuleFactory
- Creates DSPy modules dynamically
- Handles signature generation
- Supports custom input/output configurations

### 2. PipeFunction
- Main interface for pipeline execution
- Handles both immediate and optimized execution
- Manages pipeline step registration
- Provides optimization hooks

### 3. PipelineManager
- Singleton class for pipeline management
- Handles step registration and assembly
- Manages pipeline caching
- Provides pipeline assembly functionality

### 4. Metrics
- Provides evaluation metrics
- Supports custom metric implementations
- Handles exact match calculations

## Key Features

### Pipeline Execution
- Immediate execution of modules
- Optimized pipeline execution
- Input/output validation
- Error handling

### Module Management
- Dynamic module creation
- Signature generation
- Input/output field configuration
- Module chaining

### Optimization
- Pipeline caching
- Metric collection
- Optimization strategies
- Pipeline assembly

## Example Usage

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
results = pipe(application_mail_text, application_cv, 
              outputs=outputs, modules=modules)

# Optimize pipeline
optimizer = MIPROv2(metric=exact_match_metric)
optimized_pipeline = optimizer.compile(
    pipeline_manager.assemble_pipeline(),
    trainset=training_data
)
```

## File Structure

```
dspy_pipeline/
├── main.py            # Main entry point
├── module_factory.py  # Module creation
├── pipe_function.py   # Pipeline execution
├── pipeline_manager.py # Pipeline management
├── metrics.py         # Evaluation metrics
├── README.md          # Documentation
└── plan.md            # Project overview
```
