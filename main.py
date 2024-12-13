import asyncio
import argparse
from pdf_extractor.pdf_extraction import docling_pdf_extraction
from json_extractor.json_extraction import extract_json


async def main(input_file_path, output_file_path):
    extracted_pdf_raw_data = docling_pdf_extraction(input_file_path)
    extracted_json_data = await extract_json(raw_data=extracted_pdf_raw_data, output_dir=output_file_path)

    print("Extracted PDF to JSON data:")
    print(extracted_json_data)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Extract data from a PDF file and convert it to JSON.")
    parser.add_argument("-i", "--input_file_path", type=str, default="./pdf_data/sample.pdf", help="Path to the input PDF file to be processed (default: './pdf_data/照顧管理評估量表_勾選.pdf').")
    parser.add_argument("-o", "--output_file_path", type=str, default="./outputs", help="Directory where the processed JSON files will be saved (default: './outputs').")
    
    args = parser.parse_args()
    
    assert args.input_file_path.endswith(".pdf"), "The input file must be a PDF file with a '.pdf' extension."
    
    asyncio.run(main(args.input_file_path, args.output_file_path))
