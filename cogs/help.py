cmon man just make the help ur self its button pagination and ill give you the embeds here

menu = discord.Embed(title="Harley Help Menu", description="This module provides help and information about Harley's commands.", color=0x000000)
menu.add_field(name="Support", value="https://discord.gg/scene", inline=False)
menu.set_footer(text="Created by whoiskiri#0001")
menu.set_thumbnail(url=self.bot.user.avatar.url)
mod = discord.Embed(title="Moderation", description="> This module includes commands for moderating the server.", color=0x000000).add_field(name="Commands", value="ban, unban").set_footer(text="Created by whoiskiri#0001").set_thumbnail(url=self.bot.user.avatar.url),
info = discord.Embed(title="Information ", description="> This module provides information about the server and its\n> members along with the bot.", color=0x000000).add_field(name="Commands", value="ping").set_footer(text="Created by whoiskiri#0001").set_thumbnail(url=self.bot.user.avatar.url)
embeds = [
  menu,
  mod,
  info
]
