from discord import Client

class Bot(Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print("Bot is now online")

    async def on_message(self, message):
        if message.author == self.user:
            return
