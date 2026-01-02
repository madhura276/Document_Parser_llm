"""
Assisto Technologies - LLM Assignment
Task: Document Parser
Author: Madhura Gundluru
"""

from transformers import pipeline
import re

# Load LLM model
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",
    framework="pt"   # force PyTorch, avoid TensorFlow
)

def parseText(document):
    """Extract policy number from document"""
    match = re.search(r"Policy Number:\s*(\w+)", document)
    return match.group(1) if match else None

def extractData(document):
    """Extract effective and expiry dates"""
    effective = re.search(r"Effective Date:\s*(.*)", document)
    expiry = re.search(r"Expiry Date:\s*(.*)", document)

    return {
        "effectiveDate": effective.group(1) if effective else None,
        "expiryDate": expiry.group(1) if expiry else None
    }
def searchText(document):
    """Extract coverage section"""
    if "Coverage Details:" in document:
        return document.split("Coverage Details:")[1].strip()
    return None

def classifyText(coverageText):
    """Classify coverage type using LLM"""
    labels = ["liability", "collision", "comprehensive"]
    result = classifier(coverageText, labels)
    return result["labels"][0]

def validateData(data):
    """Check for missing fields"""
    return [key for key, value in data.items() if value is None]

if __name__ == "__main__":
    with open("sample_policy.txt", "r") as file:
        document = file.read()

    policy_number = parseText(document)
    dates = extractData(document)
    coverage_text = searchText(document)
    coverage_type = classifyText(coverage_text)

    extracted_data = {
        "policyNumber": policy_number,
        "effectiveDate": dates["effectiveDate"],
        "expiryDate": dates["expiryDate"],
        "coverageType": coverage_type
    }

    missing_fields = validateData(extracted_data)
        
        
    print("\n--- Extracted Data ---")
    print(extracted_data)
    print("\n--- Coverage Text ---")
    print(coverage_text)
    print("\n--- Validation Result ---")
    if missing_fields:
        print("Missing Fields:", missing_fields)
    else:
        print("No missing fields. All required data extracted successfully.")

