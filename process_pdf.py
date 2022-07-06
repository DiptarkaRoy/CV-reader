import PyPDF2
import string
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

    # characters to be excluded in tokenizer
    x=r'["\n"\!\"\#\$\%\&\'\(\)\*\,\.\/\:\;\-\<\=\>\?\[\\\]\^\_\`\{\|\}\~\" "\•\"/"\:\,\?!"]\s*'
    # create tokenizer
    tokenizer = RegexpTokenizer(x, gaps=True)

    # create tokens using RegexpTokenizer
    tokens = tokenizer.tokenize(doc)

    # return the tokens
    return tokens