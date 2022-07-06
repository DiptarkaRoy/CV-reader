import PyPDF2
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

# This function scans the pdf and converts it to lowercase and returns it
def scan(path):
    # first we open the path in the function
    file = open(path, 'rb')
    # read the file using 'PyPDF2'
    pdf = PyPDF2.PdfFileReader(file)
    # load the page
    page = pdf.getPage(0)
    # convert the content to lowercase and return the page
    return page.extractText().lower()
    # close the file
    file.close()

# This function tokenizes the contents of a file while removing punctuation and other special characters
def tokenise(path):
    # Scan the document
    doc = scan(path)

    ##Tokeniser
    # characters to be excluded in tokenizer
    x = r'["\n"\!\"\#\$\%\&\'\(\)\*\,\.\/\:\;\-\<\=\>\?\[\\\]\^\_\`\{\|\}\~\" "\•\"/"\:\,\?!"]\s*'
    # create tokenizer
    tokenizer = RegexpTokenizer(x, gaps=True)

    # create tokens using RegexpTokenizer
    tokens = tokenizer.tokenize(doc)

    # return the tokens
    return tokens

# This function removes stopwords with NLTK
def removeStopWords(tokens):
    # initialise the stopwords as a set
    stop_words = set(stopwords.words('english'))

    # Iterate through tokens and remove if the tokens are stopwords
    for w in tokens:
        if w in stop_words:
            tokens.remove(w)

    # return tokens
    return tokens