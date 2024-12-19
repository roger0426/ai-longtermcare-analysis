from flask import Flask, request, render_template, redirect, url_for
import os
import asyncio
from pdf_extractor.pdf_extraction import docling_pdf_extraction
from json_extractor.json_extraction import extract_json

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and file.filename.endswith('.pdf'):
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            # Process the PDF file
            extracted_data = asyncio.run(process_pdf(file_path))
            return render_template('result.html', extracted_data=extracted_data)
    return render_template('upload.html')

async def process_pdf(file_path):
    extracted_pdf_raw_data = docling_pdf_extraction(file_path)
    extracted_json_data = await extract_json(raw_data=extracted_pdf_raw_data, output_dir=UPLOAD_FOLDER)
    return extracted_json_data

if __name__ == '__main__':
    app.run(debug=True)
