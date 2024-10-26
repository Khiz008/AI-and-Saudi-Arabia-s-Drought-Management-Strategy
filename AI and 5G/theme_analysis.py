import os
import re
from collections import Counter

# Define the folder where your text files are located
folder_path = r"C:\Users\92317\Pictures\AI and 5G"

# Define the filenames
file_names = [
    "National Renewable Energy Program KSA.txt",
    "National Water Strategy 2030.txt",
    "Saudi Arabia's drought management strategy.txt",
    "Vision 2030.txt",
    "Paris Agreement.txt",
    "RAMSAR Convention.txt",
    "UN Convention for Combatting Diversification.txt",
    "SDG 6.txt",
    "SDG9.txt",
    "SDG 13.txt"
]

# Preprocessing function using built-in methods and regex
def preprocess_text(text):
    # Convert to lowercase and split into words using regex (keeping only alphanumeric words)
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens

# Define themes with associated keywords
themes = {
    "Drought Management": ["water", "drought", "scarcity", "conservation", "irrigation", "policy"],
    "AI and 5G": ["ai", "5g", "automation", "data", "technology", "network"],
    "Sustainability": ["sustainability", "green", "renewable", "energy", "environment"],
    "Global Agreements": ["sdg", "un", "paris", "ramsar", "international", "agreement"]
}

# Function to analyze and count theme occurrences
def analyze_themes(tokens, themes):
    theme_counts = Counter()
    for theme, keywords in themes.items():
        for keyword in keywords:
            theme_counts[theme] += tokens.count(keyword)
    return theme_counts

# Process each file and count theme occurrences
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    
    try:
        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            tokens = preprocess_text(text)
            theme_counts = analyze_themes(tokens, themes)
            
            print(f"Theme counts for {file_name}:")
            for theme, count in theme_counts.items():
                print(f"  {theme}: {count}")
    except FileNotFoundError as e:
        print(f"Error processing {file_path}: {e}")
