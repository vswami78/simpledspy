import dspy
import re

class ExtractName(dspy.Signature):
    """
    Extracts the applicant's full name from the application mail text and CV.
    """
    application_mail_text = dspy.InputField(desc="Text content of the application email.")
    application_cv = dspy.InputField(desc="Content of the applicant's CV.")
    name = dspy.OutputField(desc="Applicant's full name.")

    def __call__(self, application_mail_text: str, application_cv: str) -> str:
        # Implement logic to extract the name
        # Example: Extract the first occurrence of a proper noun after "Name:"
        match = re.search(r"Name:\s*([A-Za-z\s]+)", application_cv)
        return match.group(1).strip() if match else "Unknown"

class CheckDegree(dspy.Signature):
    """
    Checks whether the applicant possesses a specific degree.
    """
    application_mail_text = dspy.InputField(desc="Text content of the application email.")
    application_cv = dspy.InputField(desc="Content of the applicant's CV.")
    degree_bool = dspy.OutputField(desc="Boolean indicating possession of a specific degree.")

    def __call__(self, application_mail_text: str, application_cv: str) -> bool:
        # Implement logic to check for degree
        # Example: Look for "Degree: B.Sc Computer Science" in CV
        return "Degree: B.Sc Computer Science" in application_cv

class ExtractAge(dspy.Signature):
    """
    Extracts the applicant's age from the CV.
    """
    application_mail_text = dspy.InputField(desc="Text content of the application email.")
    application_cv = dspy.InputField(desc="Content of the applicant's CV.")
    age = dspy.OutputField(desc="Applicant's age.")

    def __call__(self, application_mail_text: str, application_cv: str) -> int:
        # Implement logic to extract age
        # Example: Extract the number following "Age:"
        match = re.search(r"Age:\s*(\d+)", application_cv)
        return int(match.group(1)) if match else 0
