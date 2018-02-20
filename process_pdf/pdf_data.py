
__all__ = ['using_multiprocess']


from multiprocessing import Pool
from app import logger
from .read_pdf import remove_stop_words, yield_text_from_pdf
PROCESS_POOL_SIZE = 10
logs = logger(__name__)


def process_worker(data):
    """
    the worker function supposed to read process the pdf data.
    process worker accepts data from an already processed PDF and
    then removes the stopwords.
    """
    d = None
    try:
        d = remove_stop_words(data)
    except AttributeError:
        pass
    except Exception as err:
        print(err.args[1])
    finally:
        return d


def using_multiprocess(pdfname):
    """
    this should handle the multiprocessing.
    Using the Pool multiprocess function to map the pool worker to
    map the process worker to yielded test from the PDF.
    """

    logs.info('worker {} started with pdf file {}'.format(__name__, pdfname))

    with Pool(PROCESS_POOL_SIZE) as pool:
        iterable = yield_text_from_pdf(pdfname)
        results = pool.map(process_worker, iterable)

    return results


if __name__ == '__main__':
    data = using_multiprocess('../pdf_samples/eddie_jung.pdf')
    for x in data:
        print(x)
