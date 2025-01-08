# DSPy Pipeline Code Overview

## Classes and Methods

### 1. ModuleFactory
- `create_module(inputs: List[str], outputs: List[str], description: str = "") -> dspy.Module`
  - Creates DSPy modules with specified inputs/outputs
  - Generates appropriate signatures
  - Returns Predict modules

### 2. PipeFunction
- `__init__()`
  - Initializes pipeline manager and module factory
- `optimize(optimized_pipeline: Any)`
  - Sets pipeline as optimized
  - Stores optimized pipeline
- `__call__(*args, outputs: List[str] = None, modules: List[Any] = None) -> Tuple[Any, ...]`
  - Main pipe interface
  - Handles immediate execution
  - Registers pipeline steps

### 3. PipelineManager
- `__new__()`
  - Singleton pattern implementation
  - Initializes pipeline steps and cache
- `register_step(inputs: List[str], outputs: List[str], module: Any)`
  - Registers pipeline steps
  - Stores input/output mappings
- `assemble_pipeline() -> dspy.Module`
  - Creates executable pipeline
  - Chains registered steps
  - Returns Pipeline module

### 4. Metrics
- `exact_match_metric(gold: List[Any], pred: List[Any], trace=None) -> float`
  - Calculates exact match accuracy
  - Compares predicted vs ground truth values
  - Returns accuracy score

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
