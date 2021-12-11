class Publisher:
    def __init__(self, reader, tw_bot, conf, options):
        self.options = options
        self.reader = reader
        self.tw_bot = tw_bot
        self.conf = conf

    def get_and_publish_posts(self):
        entries = self.reader.new_entries(days=self.conf.days())

        print('Announce in twitter articles published in {} in the last {} days.'.format(self.conf.name(),
                                                                                         self.conf.days()))
        print('-' * 80)

        if self.options.dry:
            print('DRY mode. No tweets will be published.')
            print('-' * 80)

        for entry in entries:
            self.__publish_entry(entry)
        else:
            print('-' * 80)
            print('Finished.')

    def __publish_entry(self, entry):
        message = 'Publicado el artículo: {} {}'.format(entry.title, entry.link)
        print(message)
        if not self.options.dry:
            self.tw_bot.say(message)
