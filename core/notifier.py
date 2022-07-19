import logging
from discord_webhook import DiscordWebhook

class DiscordNotifier:
    discord_notifier = False
    discord_endpoint = None
    
    logger = logging.getLogger("DiscordNotifer")
    
    def __init__(self, discord_notifier=False, discord_endpoint=None):
        if discord_notifier and discord_endpoint:
            self.discord_notifier = True
            self.discord_endpoint = discord_endpoint
    
    def send(self, msg):
        webhook = DiscordWebhook(url=self.discord_endpoint, content=msg)
        webhook.execute()