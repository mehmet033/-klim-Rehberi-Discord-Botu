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

PUAN_DOSYASI = "puanlar.json"
AKTIF_GOREVLER = {}  

gorevler = {
    "kolay": [...],
    "orta": [...],
    "zor": [...]
}

# Puanlar yükleniyor
def puan_yukle():
    if os.path.exists(PUAN_DOSYASI):
        with open(PUAN_DOSYASI, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

def puan_kaydet(puanlar):
    with open(PUAN_DOSYASI, "w", encoding="utf-8") as file:
        json.dump(puanlar, file, indent=4)

puanlar = puan_yukle()

@bot.event
async def on_ready():
    print(f'{bot.user.name} başarıyla başlatıldı!')

@bot.command(name="yardim")
async def yardim(ctx):
    await ctx.send(
        "🌍 **İklim Rehberi Botu Komutları:**\n"
        "1. `!gorev kolay` - Kolay bir görev verilir.\n"
        "2. `!gorev orta` - Orta zorlukta bir görev verilir.\n"
        "3. `!gorev zor` - Zor bir görev verilir.\n"
        "4. `!yaptim` - Son yapılan görevi tamamladığını bildirir, görevin zorluk seviyesine göre puan kazanılır.\n"
        "5. `!yapmadim` - Son yapılan görevi tamamlamadığını bildirir, görevin zorluk seviyesine göre puan kaybedilir.\n"
        "6. `!puan` - Şu anki toplam puanını gösterir.\n"
        "7. `!liderlik` - Puan sıralamasındaki ilk 10 oyuncuyu gösterir."
    )


@bot.command(name="gorev")
async def gorev(ctx, zorluk: str = None):
    zorluk = zorluk.lower() if zorluk else ""
    if zorluk not in gorevler:
        await ctx.send("Geçersiz veya eksik zorluk seviyesi. Kullanım: `!gorev kolay`, `!gorev orta`, `!gorev zor`")
        return
    secilen = random.choice(gorevler[zorluk])
    AKTIF_GOREVLER[str(ctx.author.id)] = zorluk
    await ctx.send(
        f"🌱 Bugünün çevreci görevi ({zorluk.title()}):\n**{secilen}**\n\n"
        f"✅ Görevi tamamladıysan `!yaptim`, ❌ tamamlamadıysan `!yapmadim` yazmayı unutma!"
    )

@bot.command(name="yaptim")
async def yaptim(ctx):
    user_id = str(ctx.author.id)
    if user_id not in AKTIF_GOREVLER:
        await ctx.send("📌 Önce bir görev alman gerekiyor! Kullanım: `!gorev kolay`, `!gorev orta`, `!gorev zor`")
        return
    zorluk = AKTIF_GOREVLER.pop(user_id)
    puan_artis = {"kolay": 50, "orta": 75, "zor": 100}.get(zorluk, 0)
    puanlar[user_id] = puanlar.get(user_id, 0) + puan_artis
    puan_kaydet(puanlar)
    await ctx.send(f"✅ {zorluk.title()} görevi tamamladın! {puan_artis} puan kazandın. Toplam puanın: **{puanlar[user_id]}**")

@bot.command(name="yapmadim")
async def yapmadim(ctx):
    user_id = str(ctx.author.id)
    if user_id not in AKTIF_GOREVLER:
        await ctx.send("📌 Önce bir görev alman gerekiyor! Kullanım: `!gorev kolay`, `!gorev orta`, `!gorev zor`")
        return
    AKTIF_GOREVLER.pop(user_id)
    puanlar[user_id] = puanlar.get(user_id, 0) - 25
    puan_kaydet(puanlar)
    await ctx.send(f"😞 Üzgünüz... 25 puan kaybettin. Toplam puanın: **{puanlar[user_id]}**")

@bot.command(name="puan")
async def puan(ctx):
    user_id = str(ctx.author.id)
    mevcut = puanlar.get(user_id, 0)
    await ctx.send(f"📊 Şu anki toplam puanın: **{mevcut}**")

@bot.command(name="liderlik")
async def liderlik(ctx):
    sirali = sorted(puanlar.items(), key=lambda x: x[1], reverse=True)
    mesaj = "🏆 Liderlik Tablosu:\n"
    for i, (kullanici_id, puan) in enumerate(sirali[:10], start=1):
        user = await bot.fetch_user(int(kullanici_id))
        mesaj += f"{i}. {user.name}: {puan} puan\n"
    await ctx.send(mesaj)


bot.run(TOKEN)
