import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "The quick brown foxes are jumping over the lazy dogs."

# Process the text
doc = nlp(text)

# Print tokens and their lemmas
for token in doc:
    print(f"Token: {token.text}, Lemma: {token.lemma_}")
