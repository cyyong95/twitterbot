import tweepy
from .helpers import validate_send_tweet


class TwitterAPI:

    t_api = None

    def __init__(self, config: dict):
        if TwitterAPI.t_api is None:
            self.__authenticate(config)

    def send_tweet(self, text: str) -> None:

        validate_send_tweet(text)

        TwitterAPI.t_api.update_status(text)

    def reauthenticate(self, config: dict) -> None:
        self.__authenticate(config)

    def __authenticate(self, config: dict) -> None:
        auth = tweepy.OAuthHandler(config["api_key"], config["api_key_secret"])
        auth.set_access_token(config["access_token"], config["access_token_secret"])
        TwitterAPI.t_api = tweepy.API(auth)
