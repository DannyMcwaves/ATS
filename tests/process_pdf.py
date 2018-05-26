"""
main test for process_pdf to see if it is working correctly
"""
import time
from process_pdf import read
PDF_FILE = "../pdf_samples/eddie_jung.pdf"

#
# def process():
#     data = getPdf(PDF_FILE)
#     for i in data:
#         print(i)


if __name__ == '__main__':
    tt1 = time.time()
    # process()
    print(read)
    tt2 = time.time()
    print(tt2 - tt1)

