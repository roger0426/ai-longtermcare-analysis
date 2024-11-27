import pdfplumber
import os


def parse_pdf(pdf_loc, page_infos: list = None):

    folder_path = '../extracted_data/' + os.path.basename(pdf_loc).split('.')[0]
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with pdfplumber.open(pdf_loc) as pdf:
        pages = pdf.pages[page_infos[0]:page_infos[1]] if page_infos else pdf.pages
        for i, page in enumerate(pages):

            words = page.extract_words()
            words_im = page.to_image()
            words_im.draw_rects(words)
            words_im.save(f'{folder_path}/words{i}.jpg')
            tables = page.extract_tables()
            with open(f'{folder_path}/table{i}.txt', 'w') as file:
                if tables is not None:
                    for table in tables:
                        if table is not None:
                            for item in table:
                                file.write(f"{item}\n")

            with open(f'{folder_path}/text{i}.txt', 'w') as file:
                file.write(page.extract_text())

            # print(page.images)
            
            checked_checkboxes = [image for image in page.images if image['srcsize'] == (14, 13)]
            notchecked_checkboxes = [image for image in page.images if image['srcsize'] == (13, 13)]

            checked_checkboxes_im = page.to_image()
            checked_checkboxes_im.draw_rects(checked_checkboxes, stroke='red')
            checked_checkboxes_im.draw_rects(notchecked_checkboxes, stroke='blue')
            checked_checkboxes_im.save(f'{folder_path}/checkbox{i}.jpg', stroke='red')

if __name__ == '__main__':
    # parse_pdf('../data/data1.pdf', [0, 11])
    # parse_pdf('../data/data2.pdf')
    parse_pdf('../data/pdf_with_marks.pdf')