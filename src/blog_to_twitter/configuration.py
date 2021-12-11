import yaml


class Configuration:
    def __init__(self):
        self.cfg = None
        self.load()

    def load(self):
        with open('config.yml', "r") as f:
            self.cfg = yaml.safe_load(f)

        self.cfg['twitter']['consumer_key']
        self.cfg['twitter']['consumer_secret']
        self.cfg['twitter']['access_token']
        self.cfg['twitter']['access_token_secret']
        self.cfg['feed']['uri']
        self.cfg['feed']['days']

    def consumer_key(self):
        return self.cfg['twitter']['consumer_key']

    def consumer_secret(self):
        return self.cfg['twitter']['consumer_secret']

    def access_token(self):
        return self.cfg['twitter']['access_token']

    def access_token_secret(self):
        return self.cfg['twitter']['access_token_secret']

    def uri(self):
        return self.cfg['feed']['uri']

    def days(self):
        return self.cfg['feed']['days']

    def name(self):
        return self.cfg['feed']['name']
