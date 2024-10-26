import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Ensure necessary NLTK data packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Directory containing the documents
directory = r"C:\Users\92317\Pictures\AI and 5G"

# Function to load and preprocess text files
def load_and_preprocess(filename):
    # Read the file
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text
    words = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    return filtered_words

# Load and preprocess all files
documents = {}
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        # Handle specific file name corrections
        if filename == "UN Convention for Combatting Diversification.txt":
            filename = "UN 1.txt"
        elif filename == "SDG9.txt":
            filename = "SDG 9.txt"
        
        filepath = os.path.join(directory, filename)
        documents[filename] = load_and_preprocess(filepath)

# Print preprocessed words from all the documents
for doc_name, words in documents.items():
    print(f"\nPreprocessed words for {doc_name}:")
    print(words[:50])  # Print first 50 words from each document
