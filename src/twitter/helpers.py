def validate_send_tweet(text: str):

    if len(text) < 1:
        raise Exception("Tweet length cannot be less than 1")

    if len(text) > 280:
        raise Exception("Tweet length cannot be more than 280")


def format_user_timeline_response(response: list) -> list:

    user_tweets: list[str] = []

    for status_object in response:

        user_tweet: str = f"Name: {status_object.user.name} | " \
                          f"Twitter handle: {status_object.user.screen_name} | " \
                          f"Tweet: {status_object.text}\n"

        user_tweets.append(user_tweet)

    return user_tweets

