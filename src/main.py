from discord import Client
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

client = Client()

client.run(TOKEN)
