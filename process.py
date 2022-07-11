import process_pdf as reader
import nltk
import os

folder = './Resumes'
files = os.listdir(folder)  # getting filenames

common_words=nltk.probability.FreqDist() # this contains the repetitive words from the set

# performing the operation for each file
for file in files:
    # Entering path
    path = folder + '/' + file
    # Cleaning Pdf
    a = reader.clean_pdf(path)
    # Mapping common words
    reader.map(a,common_words)
    print(common_words.most_common(20))