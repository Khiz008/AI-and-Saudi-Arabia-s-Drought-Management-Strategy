import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.isalpha() and word.lower() not in stop_words]
    return filtered_tokens

def identify_themes(text, keywords):
    tokens = preprocess_text(text)
    word_count = Counter(tokens)
    themes = {keyword: word_count.get(keyword, 0) for keyword in keywords}
    return themes

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Define your file paths
file_paths = [
    'C:/Users/92317/Pictures/AI and 5G/National Renewable Energy Program KSA.txt',
    'C:/Users/92317/Pictures/AI and 5G/National Water Strategy 2030.txt',
    'C:/Users/92317/Pictures/AI and 5G/Saudi Arabia drought management strategy.txt',
    'C:/Users/92317/Pictures/AI and 5G/Vision 2030.txt',
    'C:/Users/92317/Pictures/AI and 5G/Paris Agreement.txt',
    'C:/Users/92317/Pictures/AI and 5G/RAMSAR Convention.txt',
    'C:/Users/92317/Pictures/AI and 5G/UN Convention for Combatting Diversification.txt',
    'C:/Users/92317/Pictures/AI and 5G/SDG 6.txt',
    'C:/Users/92317/Pictures/AI and 5G/SDG 9.txt',
    'C:/Users/92317/Pictures/AI and 5G/SDG 13.txt'
]

# Define your keywords
keywords = ['drought', 'water', 'technology', 'sustainability', 'AI', '5G']

# Process each file
for file_path in file_paths:
    try:
        text = read_file(file_path)
        themes = identify_themes(text, keywords)
        print(f'File: {os.path.basename(file_path)}')
        print('Identified Themes:', themes)
        print('---')
    except Exception as e:
        print(f'Error processing file {file_path}: {e}')
