import preprocess as reader
folder = './Resumes'

common_words = reader.map_all(folder)

# Printing common words
keywords = reader.top_keywords(common_words, 50)
print(reader.spell_check(keywords))
