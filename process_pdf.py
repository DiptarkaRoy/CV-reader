import PyPDF2
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from autocorrect import Speller


# this function cleans the text after importing it
def clean_pdf(path):
    # scanning the file
    doc = scan(path)
    # create tokens
    tokens = spell_check(lemmatize_and_stem(removeStopWords(tokenise(doc))))
    # output
    print(tokens)
    # return tokens
    mapped=count_words(tokens)
    print(mapped)

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


# This function tokenizes the contents of a file while removing punctuation, special characters...
# ...and numbers
def tokenise(doc):
    ##Tokeniser
    # Characters to be excluded in tokenizer (including numbers)
    x = r'["\n"\!\"\#\$\%\&\'\(\)\*\,\d+\.\/\:\;\-\<\=\>\?\[\\\]\^\_\`\{\|\}\~\" "\●\○\•\"/"\:\,\?!"]\s*'
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


# This function lemmatizes the tokens
def lemmatize_and_stem(tokens):
    # lemmatizing
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(words) for words in tokens]

    # stemming
    stemmer = SnowballStemmer('english')
    tokens = [stemmer.stem(words) for words in tokens]

    # return tokens
    return tokens


# This function corrects the spelling of words spelt wrongly
def spell_check(tokens):
    spell = Speller('en')
    tokens = [spell(words) for words in tokens]
    return tokens


def count_words(tokens):
    counts = dict()
    for word in tokens:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
