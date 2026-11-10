import discord
from discord.ext import commands

# ================= CONFIG =================
TOKEN = "MTU2OTc1OTYxOTQ3ODQ1NDM1Mw.G6gnPy.uEO5_0My4w4QZn1KKEZ-cZe1wW_x1Kem9SkFpM"
WELCOME_CHANNEL_ID = 1568330042868637816  # Bdel had l'raqm b ID dyal channel dyal l'Welcome
GIF_URL = "https://files.catbox.moe/8new4j.gif" # Link dyal l'GIF dyalek

# ================= BOT SETUP =================
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"Failed to sync: {e}")

# ================= WELCOME EVENT =================
@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if not channel:
        return

    # HNA KHASSEK TBEDEL L'IDs DYAL L'CHANNELS
    # Kifach tjib l'ID: Click b l'zr l'yemni 3la l'channel f Discord -> Copy Channel ID
    RULES_ID = 1568345879080079370         # <-- 7et ID dyal #rules
    ANNOUNCEMENTS_ID = 1568330041744433215 # <-- 7et ID dyal #announcements
    PROJECTS_ID = 1568350474900471848      # <-- 7et ID dyal #projects (wla chi channel akhor)
    CHAT_ID = 1568330045783670880          # <-- 7et ID dyal #chat

    # L'Embed li ghadi yban (bhal l'image li 3titini)
    embed = discord.Embed(
        title="〢 𝟒𝐅𝐋𝐀𝐆 𝐂𝐇𝐄𝐀𝐓𝐒", # Smiyt l'embed
        description="**WELCOME TO OUR SERVER ⚡**\n\n"
                    "────────────────────\n"
                    f"📌 **Load: Check out more channels :**\n\n"
                    f"｡･ﾟ･ ➡️ Read Rules: <#{RULES_ID}>\n"
                    f"｡･ﾟ･ ➡️ Check Announcements: <#{ANNOUNCEMENTS_ID}>\n"
                    f"｡･ﾟ･ ➡️ Check WebSite: <#{PROJECTS_ID}>\n"
                    f"｡･ﾟ･ ➡️ Check Free Panels: <#{CHAT_ID}>\n\n"
                    "────────────────────\n\n"
                    "**Have a Good Time in Server ⚡**",
        color=discord.Color.blue() # Lon dyal l'khat (cyan/blue)
    )
    
    # L'Avatar dyal l'user (f l'yemni)
    embed.set_thumbnail(url=member.display_avatar.url)
    
    # L'GIF l'kbir f l'te7t
    embed.set_image(url=GIF_URL)
    
    # L'footer
    embed.set_footer(text=f"Welcome {member.name} | Member {member.guild.member_count}")

    # Sift l'message
    await channel.send(content=f"{member.mention}", embed=embed)

# ================= RUN BOT =================
if __name__ == "__main__":
    bot.run(TOKEN)