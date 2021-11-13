import tweepy
from .helpers import (
    validate_send_tweet,
    format_user_timeline_response,
    format_get_tweet_by_id,
)


class TwitterAPI:

    t_api = None
    bearer_token = ""
    api_key = ""
    api_key_secret = ""
    access_token = ""
    access_token_secret = ""

    def __init__(self, config: dict):
        if TwitterAPI.t_api is None:
            self.__authenticate(config)

    def send_tweet(self, text: str) -> None:

        validate_send_tweet(text)

        TwitterAPI.t_api.update_status(text)

    def get_tweet_by_id(self, tweet_id: int) -> dict:

        client: tweepy.Client = self.__getTwitterAPIv2Client()

        response = client.get_tweet(
            id=tweet_id, user_auth=True, expansions="referenced_tweets.id"
        )

        tweet: dict = format_get_tweet_by_id(response)

        return tweet

    def get_user_timeline_tweets(
        self, username: str, count: int, include_retweets: bool, include_replies: bool
    ) -> list[dict]:

        response: list = TwitterAPI.t_api.user_timeline(
            screen_name=username,
            count=count,
            include_rts=include_retweets,
            exclude_replies=not include_replies,
        )

        user_tweets: list[dict] = format_user_timeline_response(response)

        return user_tweets

    def reauthenticate(self, config: dict) -> None:
        self.__authenticate(config)

    def __authenticate(self, config: dict) -> None:

        TwitterAPI.bearer_token = config["bearer_token"]
        TwitterAPI.api_key = config["api_key"]
        TwitterAPI.api_key_secret = config["api_key_secret"]
        TwitterAPI.access_token = config["access_token"]
        TwitterAPI.access_token_secret = config["access_token_secret"]

        auth = tweepy.OAuthHandler(config["api_key"], config["api_key_secret"])
        auth.set_access_token(config["access_token"], config["access_token_secret"])

        TwitterAPI.t_api = tweepy.API(auth)

    def __getTwitterAPIv2Client(self) -> tweepy.Client:
        client = tweepy.Client(
            bearer_token=TwitterAPI.bearer_token,
            consumer_key=TwitterAPI.api_key,
            consumer_secret=TwitterAPI.api_key_secret,
            access_token=TwitterAPI.access_token,
            access_token_secret=TwitterAPI.access_token_secret,
        )

        return client
