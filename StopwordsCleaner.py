import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

#assigning the text sarah.txt to the sarahText global variable
sarahText = 'Sarah.txt'

#Reading the sarah.txt through the variable "sarahText", this could also be done directly as well as "Sarah.txt". We then stored the txt in the line variable.
with open(sarahText) as f:
    lines = f.readlines()

#This code retrieves a predefined list of English stopwords from the NLTK library
eng_stopwords = stopwords.words('english')

#Then we proceed to tokenize the text sample in the lines variable
text_tokens = word_tokenize(lines[0])

#Removing the stopwords from the sarah.txt text sample
without_sw = [
    word for word in text_tokens
        if not word in
                eng_stopwords
]

print(f'Here is the sarah.txt without any stopwords;\n{without_sw}')
