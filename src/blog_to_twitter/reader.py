from datetime import date, timedelta

import feedparser


def last_days(days=20):
    return (date.today() - timedelta(days=days)).timetuple()


class Reader:
    def __init__(self, uri):
        self.uri = uri
        self.entries = []

    def load(self):
        feed = feedparser.parse(self.uri)
        self.entries = feed.entries

    def new_entries(self, days=0):
        self.load()
        return filter(lambda entry: entry.published_parsed > last_days(days), self.entries)