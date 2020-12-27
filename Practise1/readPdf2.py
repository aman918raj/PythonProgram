_author_ = "aman"

import PyPDF2
import numpy as np


pdf_file = open("C:/Users/aman.raj/Desktop/files/pdf2"
                     "/xyz.pdf",'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
num_pages = read_pdf.numPages
page = read_pdf.getPage(1)
page_content = page.extractText()
print(page_content.encode("utf-8"))
pdf_file.close()
