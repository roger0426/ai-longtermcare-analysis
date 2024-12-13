import asyncio
from pdf_extractor.pdf_extraction import docling_pdf_extraction
from json_extractor.json_extraction import extract_json


async def main():
    input_file_path = "pdf_data/照顧管理評估量表_勾選.pdf"
    extracted_pdf_raw_data = docling_pdf_extraction(input_file_path)
    extracted_json_data = await extract_json(extracted_pdf_raw_data)

    print("Extracted PDF to JSON data:")
    print(extracted_json_data)

if __name__ == "__main__":
    asyncio.run(main())
