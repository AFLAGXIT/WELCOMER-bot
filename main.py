import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load l'fichier .env
load_dotenv()

# ================= CONFIG =================
TOKEN = os.getenv("DISCORD_TOKEN")  # Kay9ra l'Token mn .env
WELCOME_CHANNEL_ID = 1568330042868637816
GIF_URL = "https://files.catbox.moe/8new4j.gif"

# ================= BOT SETUP =================
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if not channel:
        return

    RULES_ID = 1568345879080079370         
    ANNOUNCEMENTS_ID = 1568330041744433215 
    PROJECTS_ID = 1568350474900471848      
    CHAT_ID = 1568330045783670880          

    embed = discord.Embed(
        title="〢 𝟒𝐅𝐋𝐀𝐆 𝐂𝐇𝐄𝐀𝐓𝐒",
        description="**WELCOME TO OUR SERVER ⚡**\n\n"
                    "────────────────────\n"
                    f"📌 **Load: Check out more channels :**\n\n"
                    f"｡･ﾟ･ ➡️ Read Rules: <#{RULES_ID}>\n"
                    f"｡･ﾟ･ ➡️ Check Announcements: <#{ANNOUNCEMENTS_ID}>\n"
                    f"｡･ﾟ･ ➡️ Check WebSite: <#{PROJECTS_ID}>\n"
                    f"｡･ﾟ･ ➡️ Check Free Panels: <#{CHAT_ID}>\n\n"
                    "────────────────────\n\n"
                    "**Have a Good Time in Server ⚡**",
        color=discord.Color.blue()
    )
    
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_image(url=GIF_URL)
    embed.set_footer(text=f"Welcome {member.name} | Member {member.guild.member_count}")

    await channel.send(content=f"{member.mention}", embed=embed)

if __name__ == "__main__":
    bot.run(TOKEN)