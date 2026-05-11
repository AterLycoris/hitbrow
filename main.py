import os
import discord
import asyncio  # 追加
from discord.ext import commands
from dotenv import load_dotenv
from database import BotDatabase

# 設定の読み込み
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class main(bot):
  def __init__(self):
    
