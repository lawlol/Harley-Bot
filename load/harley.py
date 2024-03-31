import json
from pathlib import Path
import discord
from discord.ext import commands
from aiohttp import ClientSession
from jishaku import Jishaku
import os

def get_prefix(bot, message):
  with open("cogs/json/prefixes.json", "r") as f:
    prefixes = json.load(f)

  return prefixes.get(str(message.guild.id), ';')

class Harley(commands.AutoShardedBot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=get_prefix,
            strip_after_prefix=True,
            help_command=None,
            shard_count=3,
            case_insensitive=True,
            intents=discord.Intents.all(),
            allowed_mentions=discord.AllowedMentions(
                everyone=False,
                users=True,
                roles=False,
                replied_user=False,
            ),
            activity=discord.Activity(
                type=discord.ActivityType.competing,
                name="harley, an upcoming discord bot",
            ),
            owner_ids=[ur id here],
        )
        self.ready = True
        self.run()

    def run(self) -> None:
        super().run(
            token="bot token here :wink:",
            reconnect=True,
        )

    async def on_ready(self) -> None:
      if not self.ready:
          self.ready = True
      else:
          return

      self.session = ClientSession()
      await self.load_extension("jishaku")
      await self.load_cogs()

    async def setup_hook(self):
      for file in os.listdir("./cogs"):
          if file.endswith(".py"):
              await self.load_extension("cogs." + file[:-3])
              print(f"Loaded cog: {file[:-3]}")
      await self.load_extension("jishaku")
      print(f"Loaded cog: jishaku")

bot = Harley()
