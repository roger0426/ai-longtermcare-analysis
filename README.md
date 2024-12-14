# AI Long-Term Care Analysis

A Python-based tool for extracting and analyzing long-term care assessment data from PDF documents using OCR and AI-powered text processing. This project includes a component for transforming raw data into structured formats using OpenAI's language model.

## Features

- PDF text extraction with OCR support for Traditional Chinese and English
- AI-powered JSON data extraction using OpenAI
- Structured data output in JSON format

## Prerequisites

- Python 3.10 or higher (recommended for Poetry and subfolder compatibility)
- OpenAI API key

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-longtermcare-analysis.git
   cd ai-longtermcare-analysis
   ```

2. **Install Poetry:**
   If Poetry is not installed, follow the [official installation guide](https://python-poetry.org/docs/#installation).

3. **Install project dependencies using Poetry:**
   Navigate to the `json_extractor` directory and install dependencies:
   ```bash
   poetry install
   ```

4. **Set up environment variables:**
   - Copy the provided `env` file in `json_extractor` to `json_extractor/.env`.
   - Add your OpenAI API key:
     ```bash
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

1. Place your PDF files in the `pdf_data` directory.

2. Run the main script:
   ```bash
   python -m main -i input_file_path -o output_folder_path
   ```

   Example (default):
   ```bash
   python -m main -i ./pdf_data/sample.pdf -o ./outputs
   ```

   The script will:
   1. Extract text from the PDF using OCR.
   2. Process the extracted text with OpenAI's API.
   3. Generate structured JSON output in the `outputs` directory.

## Project Structure

```
ai-longtermcare-analysis/
├── pdf_data/           # Input PDF files
├── pdf_extractor/      # PDF extraction module
├── json_extractor/     # JSON extraction module
│   ├── templates/      # JSON structure templates
│   └── env             # Example environment file
├── templates/          # JSON templates
├── outputs/            # Output JSON files
├── main.py             # Main entry point
└── requirements.txt    # Project dependencies
```

## Dependencies

- **docling:** For PDF text extraction and OCR
- **openai:** For AI-powered text processing
- **python-dotenv:** For environment variable management
- **json-repair:** For JSON string repair and validation
- **Poetry:** For dependency and environment management (preferred over `pip`)

## Example Output

The tool generates structured JSON output containing detailed assessment data. Here's a sample snippet:

```json
{
    "a": {
        "A": {
            "個案基本資料": {
                "A1": {
                    "個案婚姻狀況": {
                        "離婚": 0,
                        "分居": 0,
                        "喪偵": 1,
                        "同居": 0,
                        "未婚": 0,
                        "已婚": 0,
                        "不知道": 0
                    }
                },
                "A2": {
                    "個案教育程度": {
                        "五專": 1
                    }
                },
                "A4": {
                    "個案年齡": "50"
                }
            }
        }
    }
    // ... other assessment sections ...
}
```

The JSON output includes comprehensive assessment data across multiple sections (A through K), each containing binary indicators, text fields, or numeric values as applicable.

