import discord
import random
import json
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

def rastgele_gorev():
    with open("görevler.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return random.choice(data["görevler"])

@bot.event
async def on_ready():
    print(f'{bot.user.name} başarıyla başlatıldı!')

@bot.command(name="gorev")
async def gorev(ctx):
    görev = rastgele_gorev()
    await ctx.send(f"🌱 Bugünün görevi:\n**{görev}**")

# Botu başlat
bot.run(TOKEN)