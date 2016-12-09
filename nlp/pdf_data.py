"""
Using threads to remove to extract the raw data from the processed pdf.
"""


from multiprocessing import Process, Pool
from threading import Thread
from threading import Lock
from queue import Queue, Empty
import time
from nlp import remove_stop_words, yield_text_from_pdf
THREAD_POOL_SIZE = 10
PROCESS_POOL_SIZE = 10

# ### USING THREADS IN THIS SCENARIO ###########


class Throttle:

    def __init__(self, rate):
        """
        using token bucket algorithm for throttling.
        """
        self._consume_lock = Lock()
        self.rate = rate
        self.token = 0
        self.last = 0

    def consume(self, amount=1):
        with self._consume_lock:

            now = time.time()
            self.last = now if self.last == 0 else self.last
            elapsed = now - self.last

            if int(elapsed * self.rate):
                self.token += int(elapsed * self.rate)
                self.last = now

            # never overfill the bucket
            self.token = self.rate if self.token > self.rate else self.rate

            # dispatch tokens if available
            if self.token >= amount:
                self.token -= amount
            else:
                amount = 0

            return amount


def worker(work_queue, result_queue, throttle):
    while not work_queue.empty():
        try:
            item = work_queue.get(block=False)
        except Empty:
            break
        else:
            while not throttle.consume():
                pass
            try:
                result_queue.put(remove_stop_words(item))
            except AttributeError:
                pass
            except Exception as err:
                result_queue.put(err)
            finally:
                work_queue.task_done()


def database_writer(data):
    """
    this function will write to the database but for test purpose I will just write to a file instead.
    """
    for i in data:
        print(i)


def using_threads(pdfname):
    """
    using thread instead of futures module for concurrency.
    """
    work_queue = Queue()
    results_queue = Queue()
    throttle = Throttle(10)

    for page in yield_text_from_pdf(pdfname):
        work_queue.put(page)

    threads = [Thread(target=worker, args=(work_queue, results_queue, throttle)) for _ in range(0, THREAD_POOL_SIZE)]
    for thread in threads:
        thread.start()
    work_queue.join()

    while threads:
        threads.pop().join()

    while not results_queue.empty():
        result = results_queue.get()
        if isinstance(result, Exception):
            raise result
        database_writer(result)


# ## USIGNG MULTIPROCESSING IN THIS SCENARIO ###########


def worker2(data):
    """
    the worker function supposed to read process the pdf data.
    """
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
    """
    with Pool(PROCESS_POOL_SIZE) as pool:
        iterable = yield_text_from_pdf(pdfname)
        results = pool.map(worker2, iterable)
    for result in results:
        database_writer(result)


pdfLoc = "/media/danny_mcwaves/CODE_BASE/pyPROJECTS/ATS/uploads/french.pdf"

if __name__ == '__main__':
    t1 = time.time()
    using_multiprocess(pdfLoc)
    t2 = time.time()
    print(t2-t1)

# # time frame for threads and multi process almost the same.
