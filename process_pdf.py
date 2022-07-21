import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from autocorrect import Speller
import os


# This function finds the top words for creating keywords. Accepts a value n
def top_keywords(common_words, n):
    top_words = [w[0] for w in common_words.most_common(n)]
    return top_words


# This function finds the map of words
def map_all(folder):
    files = os.listdir(folder)  # getting filenames
    # print(files)
    common_words = nltk.probability.FreqDist()  # this contains the repetitive words from the set
    # Performing the operation for each file
    for file in files:
        # Entering path
        path = folder + '/' + file
        # Cleaning Pdf
        print(path)
        tokens = clean_pdf(path)
        print(tokens)
        # Mapping common words
        map(tokens, common_words)
    return common_words


# this function cleans the text after importing and tokenizing it
def clean_pdf(path):
    # scanning the file
    doc = scan(path)
    # create tokens
    tokens = spell_check(lemmatize_and_stem(removeStopWords(tokenise(doc))))
    # return
    return (tokens)


# This function scans the pdf and converts it to lowercase and returns it
def scan(path):
    # first we open the path in the function
    file = open(path, 'rb')
    # read the file using 'PyPDF2'
    pdf = PyPDF2.PdfFileReader(file, strict=False)
    # load the page
    page = pdf.getPage(0)

    # convert the content to lowercase and return the page
    Page = page.extract_text().lower()
    # close the file
    file.close()
    # return the page
    return Page


# This function tokenizes the contents of a file while removing punctuation, special characters...
# ...and numbers
def tokenise(doc):
    ##Tokeniser
    # Characters to be excluded in tokenizer (including numbers)
    x = r'["\n"\!\"\#\$\%\&\'\(\)\*\,\d+\.\/\:\;\-\<\=\>\?\[\\\]\^\_\`\{\|\}\~\" "\■\●\○\•\"/"\:\,\?!"]\s*'
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


# This function maps finds the frequency of words found in the tokens
def map(tokens, common_words):
    common_words += nltk.FreqDist(w for w in tokens)
