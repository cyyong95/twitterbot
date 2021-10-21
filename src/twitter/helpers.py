def validate_send_tweet(text: str):

    if len(text) < 1:
        raise Exception("Tweet length cannot be less than 1")

    if len(text) > 280:
        raise Exception("Tweet length cannot be more than 280")
