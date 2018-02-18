"""
main test for process_pdf to see if it is working correctly
"""
import time
from process_pdf import using_threads, using_multiprocess
PDF_FILE = "../pdf_samples/eddie_jung.pdf"


def thread():
    res_queue = using_threads(PDF_FILE)
    while not res_queue.empty():
        result = res_queue.get()
        print(result)


def process():
    data = using_multiprocess(PDF_FILE)
    for i in data:
        print(i)


if __name__ == '__main__':
    tt1 = time.time()
    process()
    tt2 = time.time()
    print(tt2 - tt1)

