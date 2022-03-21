# bot.py
import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix="!")

@bot.command()
async def clean(ctx, user: discord.User=None):
    messages = await ctx.history(limit=200).flatten()
    if not user:
        user_id = 393673098441785349
    else:
        user_id = user.id
    for msg in messages:
        if msg.author.id == user_id:
            await msg.delete()
            await asyncio.sleep(2)
    await ctx.send("Deleted")

bot.run(TOKEN)
