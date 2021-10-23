import helpers
import twitter.twitter as twitter


def main() -> None:

    config: dict = helpers.read_config()

    twitter_api = twitter.TwitterAPI(config)

    user_tweets: list[dict] = twitter_api.get_user_timeline_tweets(
        username="cy_yongg",
        count=1,
        include_retweets=False,
        include_replies=False)

    for user_tweet in user_tweets:
        print(user_tweet)
        print("\n")


if __name__ == '__main__':
    main()
