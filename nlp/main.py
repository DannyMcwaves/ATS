"""
PERFORMING A TRIAL TEXT FOR THE ALL THE MODULES CREATED SO FAR.
THIS WORKS BETTER.
"""
from nlp import using_multiprocess
from nlp import using_threads
from nlp import SqlInterface
import time


TABLE_NAME = "pdfData"
database = "../sqlLite/database.db"
pdfLoc = "../uploads/french.pdf"
base = SqlInterface(database)


def save_to_database(pdfname):
    """
    this saves the data to a database
    """
    data = using_multiprocess(pdfname)
    join = " ".join([" ".join(x) for x in data])
    name = pdfname.split("/")[-1]
    base.insert("1", name, join)
    print(base.fetchall())


if __name__ == '__main__':
    save_to_database(pdfLoc)