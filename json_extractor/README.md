# Formatted Data Extractor

## Description

Formatted Data Extractor is a Python package designed to convert unformatted data into a structured format. It leverages OpenAI's language model to process raw data and extract relevant information based on predefined templates.

## Installation

To install the package and its dependencies, use the following commands:

```bash
cd json_extractor
pip install poetry
poetry install
```

## Usage

### Prepare Environment
1. Copy the example environment file and rename it:
   ```bash
   cp env .env
   ```
2. Fill in your OpenAI API key in the `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

### Run the Extractor
To process the data, use the following command:

```bash
poetry run python json_extraction.py
```

### Customize Extraction
If you want to extract data from a custom format, follow these steps:

1. Add your custom example in `prompt/example_prompt.py`.
2. Place your unformatted data in the `raw_data.txt` file.

## Project Structure

- **formated_data_extractor/**
  - **prompt/**
    - `example_prompt.py`: Contains example prompts for the extraction process.
    - `extraction_prompt.py`: Contains system and user prompts for the extraction process.
  - `run_format_extractor.py`: Main script to run the data extraction process.
  - `utils.py`: Utility functions for reading templates and raw data.
  - `openai_client.py`: Client for interacting with OpenAI's API.
- **templates/**: Directory to store JSON templates.
- **raw_data.txt**: Example raw data file.

## Dependencies

- Python 3.10+
- OpenAI
- python-dotenv

