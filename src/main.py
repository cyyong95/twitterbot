import helpers
import twitter.twitter as twitter


def main() -> None:

    config: dict = helpers.read_config()

    twitter_api = twitter.TwitterAPI(config)

    user_tweets: list[dict] = twitter_api.get_user_timeline_tweets(
        username="cy_yongg",
        count=2,
        include_retweets=False,
        include_replies=True)

    for user_tweet in user_tweets:
        print(user_tweet)

    tweet = twitter_api.get_tweet_by_id(tweet_id=1452162846607826955)

    print(tweet)


if __name__ == '__main__':
    main()
