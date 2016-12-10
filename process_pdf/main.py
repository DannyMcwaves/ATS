"""
main test for process_pdf to see if it is working correctly
"""
import time
from process_pdf import using_threads, using_multiprocess
PDF_FILE = "../sample_pdf/french.pdf"


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
    # process uses approximately 0.90s and thread uses 0.92s on my machine.

