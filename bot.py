import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.tree.command(name="ban-us-adan", description="Disconnects everyone from your voice channel.", guild=discord.Object(id=GUILD_ID))
async def ban_us_adan(interaction: discord.Interaction):
    await interaction.response.defer()  # Acknowledge command

    member = interaction.user
    if not member.voice or not member.voice.channel:
        await interaction.followup.send("You must be in a voice channel to use this!", ephemeral=True)
        return

    channel = member.voice.channel
    if not channel.permissions_for(channel.guild.me).move_members:
        await interaction.followup.send("I lack permission to move members!", ephemeral=True)
        return

    for voice_member in channel.members:
        await voice_member.move_to(None)

    await interaction.followup.send("bye bye!")

@bot.tree.command(name="gnight-girl", description="twomad sleeping!", guild=discord.Object(id=GUILD_ID))
async def gnight_girl(interaction: discord.Interaction):
    await interaction.response.send_message("https://tenor.com/view/twomad-happy-laugh-fall-gif-14365056")

bot.run(TOKEN)

