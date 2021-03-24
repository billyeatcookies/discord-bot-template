from discord.ext.commands import Bot
from data.Extensions import Extensions
from data.config import Config


class Client(Bot):
    """
    doc
    """
    def __init__(self, _extensions: Extensions, command_prefix, **options):
        super().__init__(command_prefix, **options)
        self.load_extensions(_extensions)

    def load_extensions(self, _extensions):
        for extension in _extensions.get_all_extensions():
            self.load_extension(extension)


config = Config()
extensions = Extensions()

client = Client(extensions, config.get_prefix())
client.run(config.get_token())
