import tweepy


class TwBot:
    def __init__(self, configuration):
        auth = tweepy.OAuthHandler(configuration.consumer_key(), configuration.consumer_secret())
        auth.set_access_token(configuration.access_token(), configuration.access_token_secret())

        self.api = tweepy.API(auth)

    def say(self, message):
        self.api.update_status(status=message)