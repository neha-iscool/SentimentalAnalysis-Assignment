import tweepy                                
import pandas as pd                         
import numpy as np                          
from IPython.display import display
from re import clean_tweet
from get_polaority import Get_polarity

consumerkey       = 'XXXXXXXXXXXXXXXXXXXXXXXXX' 
consumersecret    = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
accesstoken       = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
accesstokensecret = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'

def info_extraction(): 
    oauth = tweepy.OAuthHandler(consumerkey, consumersecret) 
    oauth.set_access_token(accesstoken, accesstokensecret)    
    connection = tweepy.API(oauth)                            
    return connection      
    
connection = info_extraction()                                                
tweets = connection.user_timeline(screen_name="GIVE A TWITTER USERNAME", count=100)    
print("Number of tweets that are extracted: {}\n".format(len(tweets))) 
print("10 recent tweets:\n")
for x in tweets[:10]:
    print(x.text)                                                             

data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
data['Sentiment analysis'] = np.array([ clean_tweet(tweet) for tweet in data['Tweets'] ])
data['Polarity']=np.array([get_polarity(tweet) for tweet in data['Tweets']])

positive_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['Polarity'][index] > 0]
neutral_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['Polarity'][index] == 0]
negative_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['Polarity'][index] < 0]

postive_tweets

negative_tweets

neutral_tweets
    
    
    
    
