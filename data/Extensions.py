"""
extensions
"""
import json


class Extensions:
    def __init__(self):
        self.events_cog = "events"
        self.load_extensions()

    def load_extensions(self):
        self.load_events_cog()

    def load_events_cog(self):
        with open("data/extensions.json") as file:
            data = json.load(file)
            self.events_cog = data[self.events_cog]

    def get_events_cog(self):
        return self.events_cog

    def get_all_extensions(self):
        return [self.get_events_cog()]
