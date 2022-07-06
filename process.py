import process_pdf as reader

a = reader.tokenise('./Resumes/Resume_of_Diptarka_Roy.pdf')
print(a)
b = reader.removeStopWords(a)
print(b)