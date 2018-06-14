from textblob import TextBlob
def get_polarity(tweet):
  analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0: return 1
    elif analysis.sentiment.polarity == 0: return 0
    else: return -1
