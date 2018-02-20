"""
NATURAL LANGUAGE PROCESSING
"""
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
import PyPDF2


__all__ = ["remove_stop_words", "yield_text_from_pdf"]
# nltk.data.path.append('/Users/macbookpro/big_data/nltk_data')


def yield_text_from_pdf(pdfname):
    """
    yield the pages from a pdf file.
    """

    # open the pdf file as you would open any other binary file.
    with open(pdfname, "rb") as file:
        pdf = PyPDF2.PdfFileReader(file)

        # loop through the number of pages and yield content
        for i in range(0, pdf.numPages):
            page = pdf.getPage(i)
            yield page.extractText()


def detect_language(text):
    """
    detecting and returning the language of the pdf file.
    """

    # tokenize the text and remove duplicates.
    tokens = wordpunct_tokenize(text)
    words = {x.lower() for x in tokens}

    # A dictionary of the various languages and the corresponding len of stopwords in the pdf file.
    languages = {x: len(words.intersection({i for i in stopwords.words(x)})) for x in stopwords.fileids()}

    # the language with max stopwords in the pdf file.
    return max(languages, key=languages.get)


def remove_stop_words(text):
    """
    removes all the stopwords from the text and returns a list of the remaining words.
    tokenize the yielded pages from the pdf file.
    remove all stopwords and return a list of actual words.
    """
    tokenize = {x for x in wordpunct_tokenize(text)}
    stopwords_list = stopwords.words(detect_language(text))
    return [x for x in tokenize if x not in stopwords_list and len(x) > 1 and
            (x.isalnum() or x.isalpha() or x.isdigit() or x.isdecimal())]
