from pipe_function import pipe
from dsp_modules import ExtractName, CheckDegree, ExtractAge
from pipeline_manager import PipelineManager
from metrics import exact_match_metric
from dspy.teleprompt import MIPROv2
from typing import List, Dict, Any, Tuple

# Instantiate DSPy modules
extract_name = ExtractName()
check_degree = CheckDegree()
extract_age = ExtractAge()

# Define an application processing function
def process_application(application_mail_text: str, application_cv: str) -> Tuple[str, bool, int]:
    """
    Processes a single application by extracting name, degree status, and age.
    
    Args:
        application_mail_text (str): Text content of the application email.
        application_cv (str): Content of the applicant's CV.
    
    Returns:
        Tuple[str, bool, int]: A tuple containing (name, degree_bool, age).
    """
    name, degree_bool, age = pipe(
        application_mail_text,
        application_cv,
        outputs=["name", "degree_bool", "age"],
        modules=[extract_name, check_degree, extract_age]
    )
    return name, degree_bool, age

# Define a function to process multiple applications
def process_multiple_applications(applications: List[Dict[str, str]]) -> List[Tuple[str, bool, int]]:
    """
    Processes multiple applications by making multiple pipe calls.
    
    Args:
        applications (List[Dict[str, str]]): List of applications with 'application_mail_text' and 'application_cv'.
    
    Returns:
        List[Tuple[str, bool, int]]: List of tuples containing the outputs for each application.
    """
    results = []
    for app in applications:
        name, degree_bool, age = pipe(
            app['application_mail_text'],
            app['application_cv'],
            outputs=["name", "degree_bool", "age"],
            modules=[extract_name, check_degree, extract_age]
        )
        results.append((name, degree_bool, age))
    return results

# Main execution
if __name__ == "__main__":
    # Sample applications
    applications = [
        {
            "application_mail_text": """
                Dear Hiring Manager,

                I am excited to apply for the Data Scientist position. With a Ph.D. in Statistics and three years of experience...

                Sincerely,
                Alice Smith
            """,
            "application_cv": """
                Name: Alice Smith
                Degree: Ph.D. Statistics
                Age: 28
                Experience:
                - Data Analyst at DataCorp (2020-2023)
                Skills: Python, R, Machine Learning
            """
        },
        {
            "application_mail_text": """
                Dear Hiring Team,

                I am applying for the Marketing Manager role. I hold an MBA and have over five years of experience in digital marketing...

                Regards,
                Bob Johnson
            """,
            "application_cv": """
                Name: Bob Johnson
                Degree: MBA
                Age: 35
                Experience:
                - Marketing Specialist at MarketHub (2015-2020)
                Skills: SEO, Content Marketing, Analytics
            """
        }
    ]

    # Register pipeline steps by processing multiple applications
    results_before_optimization = process_multiple_applications(applications)
    print("Immediate Results Before Optimization:")
    for idx, (name, degree_bool, age) in enumerate(results_before_optimization, 1):
        print(f"Application {idx}:")
        print(f"  Name: {name}")
        print(f"  Has Degree: {degree_bool}")
        print(f"  Age: {age}\n")

    # Assemble the pipeline
    pipeline_manager = PipelineManager()
    assembled_pipeline = pipeline_manager.assemble_pipeline()

    # Initialize the optimizer
    optimizer = MIPROv2(
        metric=exact_match_metric,
        auto="light",  # Optimization mode: "light", "medium", "heavy"
        num_threads=24  # Adjust based on available resources
    )

    # Define a representative training set
    trainset = [
        {
            "input1": "Dear Hiring Manager, I am applying...",
            "input2": "Name: Jane Doe\nDegree: B.Sc Computer Science\nAge: 28...",
            "name": "Jane Doe",
            "degree_bool": True,
            "age": 28
        },
        {
            "input1": "Dear Hiring Team, I am applying...",
            "input2": "Name: Bob Johnson\nDegree: MBA\nAge: 35...",
            "name": "Bob Johnson",
            "degree_bool": True,
            "age": 35
        }
    ]

    # Compile (optimize) the program
    optimized_pipeline = optimizer.compile(
        program=assembled_pipeline,
        trainset=trainset
    )

    # Save the optimized pipeline to cache (optional)
    optimized_pipeline.save("optimized_pipeline.json")
    print("Optimized pipeline has been compiled and saved.\n")

    # Execute the optimized pipeline for each application
    print("Optimized Results After Pipeline Optimization:")
    for idx, app in enumerate(applications, 1):
        optimized_outputs = optimized_pipeline(
            input1=app['application_mail_text'],
            input2=app['application_cv']
        )
        optimized_name, optimized_degree_bool, optimized_age = optimized_outputs
        print(f"Application {idx}:")
        print(f"  Name: {optimized_name}")
        print(f"  Has Degree: {optimized_degree_bool}")
        print(f"  Age: {optimized_age}\n")
