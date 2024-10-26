from textblob import TextBlob
import os

# Define a function for sentiment analysis
def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the polarity: range from -1 (negative) to 1 (positive)
    return blob.sentiment.polarity

# Directory containing your text files
directory = "C:/Users/92317/Pictures/AI and 5G/"

# Define the themes you're analyzing
themes = ["Drought Management", "AI and 5G", "Sustainability", "Global Agreements"]

# Store sentiment results
sentiment_results = {}

# Iterate through the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
            # Analyze the sentiment of the entire text
            sentiment_score = analyze_sentiment(text)
            
            # Add sentiment score to the results
            sentiment_results[filename] = sentiment_score

# Display sentiment results
for file, score in sentiment_results.items():
    sentiment = "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"
    print(f"Sentiment for {file}: {sentiment} (Score: {score:.2f})")
