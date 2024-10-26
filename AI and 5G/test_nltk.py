import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "This is a simple test sentence."

# Tokenize the text
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("Filtered Tokens:", filtered_tokens)
