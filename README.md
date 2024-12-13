Here's the complete README.md file in a single markdown block:

```markdown
# AI Long-term Care Analysis

A Python-based tool for extracting and analyzing long-term care assessment data from PDF documents using OCR and AI-powered text processing.

## Features

- PDF text extraction with OCR support for Traditional Chinese and English
- AI-powered JSON data extraction using OpenAI
- Structured data output in JSON format

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-longtermcare-analysis.git
cd ai-longtermcare-analysis
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Place your PDF files in the `pdf_data` directory

2. Run the main script:
```bash
python -m main
```

The script will:
1. Extract text from the PDF using OCR
2. Process the extracted text using OpenAI's API
3. Generate structured JSON output in the `outputs` directory

## Project Structure

```
ai-longtermcare-analysis/
├── pdf_data/           # Input PDF files
├── pdf_extractor/      # PDF extraction module
├── json_extractor/     # JSON extraction module
├── templates/          # JSON templates
├── outputs/            # Output JSON files
├── main.py            # Main entry point
└── requirements.txt   # Project dependencies
```

## Dependencies

- docling: For PDF text extraction and OCR
- openai: For AI-powered text processing
- python-dotenv: For environment variable management
- json-repair: For JSON string repair and validation

## License

[Add your license information here]

## Contributing

[Add contribution guidelines if applicable]

## Example Output

The tool generates structured JSON output containing detailed assessment data. Here's a sample output:

```json
{
    "a": {
        "A": {
            "個案基本資料": {
                "A1": {
                    "個案婚姻狀況": {
                        "離婚": 0,
                        "分居": 0,
                        "喪偶": 1,
                        "同居": 0,
                        "未婚": 0,
                        "已婚": 0,
                        "不知道": 0
                    }
                },
                "A2": {
                    "個案教育程度": {
                        "五專": 1,
                        // ... other education fields ...
                    }
                },
                "A3": {
                    "個案身分別": {
                        // ... identity fields ...
                    }
                },
                "A4": {
                    "個案年齡": "50"
                }
            }
        }
    },
    // ... other assessment sections (B through K) ...
}
```

The JSON output includes comprehensive assessment data across multiple sections:
- Section A: Basic case information (個案基本資料)
- Section B: Primary and secondary caregiver information
- Section C: Communication ability
- Section D: Short-term memory assessment
- Section E: Daily activity function scale
- Section F: Instrumental activities of daily living
- Section G: Special complex care needs
- Section H: Home environment and social participation
- Section I: Emotional and behavioral patterns
- Section J: Primary caregiver burden
- Section K: Caregiver work and support

Each field uses binary values (0 or 1) to indicate selections, with some fields containing text or numeric values where appropriate.