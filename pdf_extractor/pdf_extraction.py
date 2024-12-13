from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, EasyOcrOptions
from docling.document_converter import PdfFormatOption, DocumentConverter


def docling_pdf_extraction(file_name: str):
    pipeline_options = PdfPipelineOptions(do_ocr = True, ocr_options = EasyOcrOptions(lang=["ch_tra","en"]))

    pdfFormatOption = PdfFormatOption(pipeline_options=pipeline_options)

    doc_converter = DocumentConverter(
        format_options={InputFormat.PDF: pdfFormatOption}
    )

    return doc_converter.convert(file_name).document.export_to_markdown()