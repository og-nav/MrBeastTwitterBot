import tweepy
import os
from dotenv import load_dotenv

def post_tweet():
  load_dotenv()
  API_KEY = os.getenv('API_KEY')
  API_SECRET = os.getenv('API_SECRET')
  ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
  ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

  auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  api = tweepy.API(auth)

  tweets = api.user_timeline(screen_name='trustfundpro')
  yesterday = int(tweets[0].text.split(' ')[1])
  new_tweet = f'Day {yesterday + 1} of asking @MrBeast for $10,000'
  media = api.media_upload('bernie.jpg')
  post = api.update_status(status=new_tweet, media_ids=[media.media_id])

post_tweet()