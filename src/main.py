import helpers
import twitter.twitter as twitter


def main() -> None:

    config: dict = helpers.read_config()

    twitter_api = twitter.TwitterAPI(config)

    twitter_api.send_tweet("Hello world!")


if __name__ == '__main__':
    main()
