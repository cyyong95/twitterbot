import tweepy
from .helpers import validate_send_tweet, \
    format_user_timeline_response


class TwitterAPI:

    t_api = None

    def __init__(self, config: dict):
        if TwitterAPI.t_api is None:
            self.__authenticate(config)

    def send_tweet(self, text: str) -> None:

        validate_send_tweet(text)

        TwitterAPI.t_api.update_status(text)

    def get_user_timeline_tweets(self,
                          username: str,
                          count: int,
                          include_retweets: bool,
                          include_replies: bool) -> list[str]:

        response: list = TwitterAPI.t_api.user_timeline(
            screen_name=username,
            count=count,
            include_rts=include_retweets,
            exclude_replies=not include_replies)

        user_tweets: list[str] = format_user_timeline_response(response)

        return user_tweets

    def reauthenticate(self, config: dict) -> None:
        self.__authenticate(config)

    def __authenticate(self, config: dict) -> None:
        auth = tweepy.OAuthHandler(config["api_key"], config["api_key_secret"])
        auth.set_access_token(config["access_token"], config["access_token_secret"])
        TwitterAPI.t_api = tweepy.API(auth)
