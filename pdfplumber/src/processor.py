import pdfplumber
import os


def parse_pdf(pdf_loc, page_infos: list = None):

    dir_path = os.path.join('../extracted_data/', os.path.basename(pdf_loc).split('.')[0])

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    text = ""
    with pdfplumber.open(pdf_loc) as pdf:
        pages = pdf.pages[page_infos[0]:page_infos[1]] if page_infos else pdf.pages
        for i, page in enumerate(pages):

            words = page.extract_words()
            words_im = page.to_image()
            words_im.draw_rects(words)
            words_im.save(os.path.join(dir_path, f'words{i}.jpg'))

            tables = page.extract_tables()
            with open(os.path.join(dir_path, f'table{i}.txt'), 'w') as file:
                if tables is not None:
                    for table in tables:
                        if table is not None:
                            for item in table:
                                file.write(f"{item}\n")


            text += page.extract_text() + '\n'
            with open(os.path.join(dir_path, f'text{i}.txt'), 'w') as file:
                file.write(page.extract_text())

            
            checked_checkboxes = [image for image in page.images if image['srcsize'] == (14, 13)]
            notchecked_checkboxes = [image for image in page.images if image['srcsize'] == (13, 13)]

            checked_checkboxes_im = page.to_image()
            checked_checkboxes_im.draw_rects(checked_checkboxes, stroke='red')
            checked_checkboxes_im.draw_rects(notchecked_checkboxes, stroke='blue')
            checked_checkboxes_im.save(os.path.join(dir_path, f'checkbox{i}.jpg'), stroke='red')
    with open(os.path.join(dir_path, f'text_all.txt'), 'w') as file:
        file.write(text)

if __name__ == '__main__':
    parse_pdf('../data/照顧管理評估量表_勾選.pdf')