import process_pdf as reader

a = reader.tokenise('./Resumes/debika_piriya_dharmalingam - debika piriya.pdf')
print(a)
b = reader.removeStopWords(a)
print(b)
