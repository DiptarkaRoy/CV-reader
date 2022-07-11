import process_pdf as reader
import os

folder='./Resumes'
files=os.listdir(folder) #getting filenames

#performing the operation for each file
for file in files:
    path=folder+'/'+file
    print(path)
    a = reader.clean_pdf(path)