import discord
from discord import app_commands
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="start", description="Start the Minecraft server")
async def start(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Minecraft server startup requested!"
    )

bot.run(TOKEN)
