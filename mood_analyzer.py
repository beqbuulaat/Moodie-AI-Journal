from textblob import TextBlob

def analyze_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "позитивное"
    elif polarity < -0.2:
        return "негативное"
    else:
        return "нейтральное"
