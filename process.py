import process_pdf as reader

a=reader.tokenise('./Resumes/Resume_of_Diptarka_Roy.pdf')
b=reader.tokeniseReg('./Resumes/Resume_of_Diptarka_Roy.pdf')
print(a)
print(b)