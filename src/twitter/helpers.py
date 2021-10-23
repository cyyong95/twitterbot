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

