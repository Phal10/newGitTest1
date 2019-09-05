from textblob import TextBlob
val = TextBlob(input("Enter your Comment: "))
print( val.tags )
print("Sentiment:", val.sentiment.polarity)
print(val.words[1].singularize())