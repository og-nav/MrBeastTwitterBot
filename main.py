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


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    post_tweet()
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

def main():
  post_tweet()

if __name__ == "__main__":
    main()
    #app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

  