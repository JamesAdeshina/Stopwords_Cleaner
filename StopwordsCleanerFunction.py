from tokenize import tokenize

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensuring the NLTK data is downloaded
nltk.download('stopwords')
nltk.download('punkt')


# Function to read text from a file
def read_text_from_file(filepath):
    with open(filepath, 'r') as file:
        return file.readlines()

# Function to retrieve English stopwords from NLTK
def get_stopwords():
    return stopwords.words('english')

# Function to tokenize text
def tokenize_text(text):
    return word_tokenize(text)

# Function to remove stopwords from tokenized text
def remove_stopword(tokens, stopword_list):
    return[
        word for word in tokens if word.lower() not in stopword_list
    ]

# Main function to process the text
def processing_text(filepath):
    # Read the text file
    lines = read_text_from_file(filepath)

    # Tokenize the text (assumes the first line is the text to be processed)
    text_tokens = tokenize_text(lines[0])

    # Get the stopwords
    eng_stopwords = get_stopwords()

    # Remove stopwords
    filtered_tokens = remove_stopword(text_tokens, eng_stopwords)

    return filtered_tokens

# Path to the text file
sarahText = 'data/Sarah.txt'

# Process the text and print the result
result = processing_text(sarahText)
print(f'Here is Sarah.txt without any stopwords;\n {result}')