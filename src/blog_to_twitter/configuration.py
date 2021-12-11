import os

import yaml


class Configuration:
    def __init__(self, options):

        if not os.path.isfile(options.config_file):
            raise Exception('File {} not found'.format(options.config_file))

        self.config_file = options.config_file
        self.cfg = None
        self.load()
        self.override_with_cli(options)

    def load(self):
        with open(self.config_file, "r") as file:
            self.cfg = yaml.safe_load(file)

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

    def override_with_cli(self, options):
        if options.days:
            self.override_days(options.days)

    def override_days(self, days):
        self.cfg['feed']['days'] = days
