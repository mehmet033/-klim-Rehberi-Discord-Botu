import discord
import random
import json
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

gorevler = [
    "Bugün musluğu açık bırakmadan diş fırçala.",
    "Elektronik cihazları kullanmadığında fişten çek.",
    "Gereksiz yere ışıkları açık bırakma.",
    "Plastik poşet yerine bez çanta kullan.",
    "Bugün çöpünü ayırarak geri dönüşüme katkı sağla.",
    "Bugün yürümeyi veya bisikleti tercih et!",
    "Doğaya zarar vermeyen bir temizlik ürünü kullan.",
    "Gıda israfını azaltmak için yiyeceklerini planla."
]

@bot.event
async def on_ready():
    print(f'{bot.user.name} başarıyla başlatıldı!')

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(
                "🌍 Merhaba! Ben İklim Rehberi Botu, buradayım çünkü dünya yardıma ihtiyaç duyuyor!\n"
                "🌱 Her gün küçük bir adımla iklim değişikliğiyle mücadele edebiliriz!"
            )
            break

@bot.command(name="gorev")
async def gorev(ctx):
    secilen = random.choice(gorevler)
    await ctx.send(f"🌱 Bugünün çevreci görevi:\n**{secilen}**")


bot.run(TOKEN)
