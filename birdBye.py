from config import settings
from tqdm import tqdm
import tweepy


# API credentials. Either from .secrets.toml or you can hardcode yours in here
consumer_key = settings.api_key
consumer_secret = settings.api_key_secret
access_token = settings.access_token
access_token_secret = settings.access_token_secret
bearer_token = settings.bearer_token
user_id = settings.user_id

# set up the authentication and connect to the api
auth = tweepy.OAuth1UserHandler(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

api = tweepy.API(auth)

# query and delete all tweets
print("Removing all tweets")
for status in tqdm(tweepy.Cursor(api.user_timeline).items()):
    api.destroy_status(status.id)

# query and delete all follows
print("Removing all follows")
for following in tqdm(tweepy.Cursor(api.get_friend_ids).items()):
    api.destroy_friendship(user_id=following)

# set up user client to delete favorites
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

# find and delete likes/favorites, login if needed
print("Removing all likes")
liked_tweets = client.get_liked_tweets(user_id, user_auth=True)

# crude pagination loop through all likes
try:
    while len(liked_tweets.data) > 0:
        for tweet in tqdm(liked_tweets.data):
            api.destroy_favorite(tweet.id)
        liked_tweets = client.get_liked_tweets(
            settings.user_id,
            pagination_token=liked_tweets.meta[
                "next_token"
            ],  # honestly not sure if needed
            user_auth=True,
        )

except TypeError:
    pass

print("All done!")
