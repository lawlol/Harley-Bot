import discord
from discord.ext import commands
from discord.ext.commands import command

class Information(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="ping")
  async def ping(self, ctx):
    ping = round(self.bot.latency * 1000)
    pingembed = discord.Embed(description=f"> {ctx.author.mention} my current ping is **{ping}ms**", color=0x000000)
    await ctx.send(embed=pingembed)

async def setup(bot):
  await bot.add_cog(Information(bot))
