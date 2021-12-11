import sys


class CliOptions:
    def __init__(self):
        self.config_file = 'config.yml'
        self.dry = False
        self.days = None
        self.load()

    def load(self):
        cli_options = sys.argv[1:]

        for index, option in enumerate(cli_options):
            if option == '-c':
                self.config_file = cli_options[index + 1]
            if option == '--dry':
                self.dry = True
            if option == '--days':
                self.days = int(cli_options[index + 1])
