import logging
from discord_webhook import DiscordWebhook

class DiscordNotifier:
    discord = False
    discord_endpoint = None
    
    logger = logging.getLogger("DiscordNotifer")
    
    def __init__(self, discord=False, discord_endpoint=None):
        if discord and discord_endpoint:
            self.discord = True
            self.discord_endpoint = discord_endpoint

    def send(self, msg):
        if self.discord:
            webhook = DiscordWebhook(url=self.discord_endpoint, content=msg)
            webhook.execute()
