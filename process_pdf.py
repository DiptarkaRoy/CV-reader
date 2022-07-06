import PyPDF2
import nltk
from nltk.tokenize import RegexpTokenizer


def scan(path):
    # first we open the path in the function
    file = open(path, 'rb')
    # read the file using 'PyPDF2'
    pdf = PyPDF2.PdfFileReader(file)
    # load the page
    page = pdf.getPage(0)
    # return the page
    return page.extractText()
    # close the file
    file.close()


def tokenise(path):
    # Scan the document
    doc = scan(path)
    # create tokens using word_tokenize
    tokens = nltk.word_tokenize(doc)
    # return the tokens
    return tokens


def tokeniseReg(path):
    # Scan the document
    doc = scan(path)
    # create tokenizer
    tokenizer = RegexpTokenizer(r'["\n"\" "\•\:\,\?!"]\s*', gaps=True)
    # create tokens using RegexpTokenizer
    tokens = tokenizer.tokenize(doc)
    # return the tokens
    return tokens
