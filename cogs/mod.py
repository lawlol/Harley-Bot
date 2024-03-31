import discord
from discord.ext import commands
from discord.ext.commands import command

class Moderation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="ban")
  async def ban(self, ctx: commands.Context, member: discord.Member=None, *, reason=None):
    if member is None:
      banhelp = discord.Embed(title="Ban Member", color=0x000000)
      banhelp.add_field(name="Parameters", value="member & reason[optional]", inline=False)
      banhelp.add_field(name="Permissions", value="ban members", inline=False)
      banhelp.add_field(name="Usage", value=f"```Syntax: ;ban @member [reason]\nExample: ;ban @law Loser```")
      await ctx.send(embed=banhelp)
      return

    if reason is None:
      reason = "No reason specified"
      return

    if ctx.author.guild_permissions.ban_members:
      await member.ban(reason=f"Banned by {ctx.author.name}")
      await ctx.send(f"> banned {member.mention}.")

  @commands.command(name="unban")
  async def unban(self, ctx: commands.Context, *, member: discord.User=None):
      if member is None:
          unbanhelp = discord.Embed(title="Unban Member", color=0x000000)
          unbanhelp.add_field(name="Parameters", value="member", inline=False)
          unbanhelp.add_field(name="Permissions", value="ban members", inline=False)
          unbanhelp.add_field(name="Usage", value=f"```Syntax: ;unban userid\nExample: ;unban 1205306615570374689```")
          await ctx.send(embed=unbanhelp)
          return

      guild = ctx.guild
      embed = discord.Embed(description=f"> unbanned {member}.", color=0x000000)
      await guild.unban(user=member)
      await ctx.send(embed=embed)

  @command(name="lawban")
  async def lawban(self, ctx, member: discord.Member = None):
    if member is None:
      banhelp = discord.Embed(title="Ban Member", description="```<> = required\n[] = not required```", color=0x000000)
      banhelp.add_field(name="Parameters", value="<member> & [reason]", inline=False)
      banhelp.add_field(name="Permissions", value="ban members", inline=False)
      banhelp.add_field(name="Usage", value=f"```Syntax: ;ban @member [reason]\nExample: ;ban @law Loser```")
      await ctx.send(embed=banhelp)
      return

    if ctx.author.guild_permissions.ban_members:
      await member.ban(Reason=f"Banned by {ctx.author.name}")
      await ctx.send(f"Banned {member.mention}")

async def setup(bot):
  await bot.add_cog(Moderation(bot))
