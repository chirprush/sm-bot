from bot import Bot
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

client = Bot()

client.run(TOKEN)
