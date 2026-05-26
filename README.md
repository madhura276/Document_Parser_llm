# Document Parser

### Problem Statement
Insurance policy documents are often lengthy and difficult to understand.
The objective of this task is to build an LLM-powered document parser that can
process insurance policy text, extract key information, classify coverage type,
and validate required fields in a structured and explainable manner.

---

## Approach
The solution follows the logical steps provided in the assignment and maps them
directly to implemented functions:

1. **parseText()**
   - Extracts the policy number from the document using pattern matching.

2. **extractData()**
   - Extracts important dates such as effective date and expiry date.

3. **searchText()**
   - Identifies and extracts the coverage-related section from the document.

4. **classifyText()**
   - Uses a Large Language Model (LLM) with zero-shot classification to classify
     the coverage type as liability, collision, or comprehensive.

5. **validateData()**
   - Validates the extracted data by checking for missing required fields.

Intermediate outputs such as coverage text and validation results are displayed
to clearly demonstrate each processing step.

---
**LLM Usage:**
A pre-trained transformer-based Large Language Model
(`facebook/bart-large-mnli`) is used in the classifyText() step to perform
semantic zero-shot classification of insurance coverage text. This enables
intelligent classification without task-specific model training.


## Technologies Used
- Python 3.10
- HuggingFace Transformers
- PyTorch
- Zero-shot Classification (LLM-based NLP)

---

## Project Structure

```text
document-parser-llm/
├── app.py
├── sample_policy.txt
├── requirements.txt
└── README.md
```

---

## How to Run
**1. Install dependencies:**
```bash
pip install -r requirements.txt

**2. Run the application:**
```bash
python app.py

## Output

The system displays:
Extracted coverage text
Structured policy information (policy number, dates, coverage type)
Validation results indicating whether required fields are present
The output remains consistent for the same input document, ensuring reliability
and correctness of the document parsing process.
