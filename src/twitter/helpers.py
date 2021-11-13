def validate_send_tweet(text: str):

    if len(text) < 1:
        raise Exception("Tweet length cannot be less than 1")

    if len(text) > 280:
        raise Exception("Tweet length cannot be more than 280")


def format_user_timeline_response(response: list) -> list[dict]:

    user_tweets: list[dict] = []

    for status_object in response:

        user_tweet: dict = {
            "tweet_id": status_object.id,
            "name": status_object.user.name,
            "twitter_username": status_object.user.screen_name,
            "tweet": status_object.text,
            "retweet_count": status_object.retweet_count,
            "favourite_count": status_object.favorite_count,
            "tweet_created_at": f"{status_object.created_at}",
        }

        user_tweets.append(user_tweet)

    return user_tweets


def format_get_tweet_by_id(response) -> dict:

    response_data = response.data
    response_includes_tweets = response.includes.get("tweets")

    parent_tweets: list[dict] = []

    for tweet in response_includes_tweets:
        parent_tweets.append(
            {"parent_tweet_id": tweet.id, "parent_tweet_text": tweet.text}
        )

    tweet: dict = {
        "tweet_id": response_data.id,
        "tweet_text": response_data.text,
        "parent_tweets": parent_tweets,
    }

    return tweet
