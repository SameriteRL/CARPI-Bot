import datetime as dt
import random

import discord
from discord.ext import commands
from discord.ext.commands import CommandError, Context

from bot import CARPIBot
from globals import BAD_MEMBER_MSG, ERROR_TITLE, send_generic_error


class Miscellaneous(commands.Cog):
    def __init__(self, bot: CARPIBot):
        self.bot = bot

    async def cog_command_error(self, ctx: Context, error: CommandError) -> None:
        if not ctx.command.has_error_handler():
            await send_generic_error(ctx, error)

    ### PING ###
    @commands.hybrid_command(
        description = "Pong!"
    )
    async def ping(self, ctx: Context):
        # Gets the bot to server latency in milliseconds
        embedVar = discord.Embed(
            title = "Pong!",
            description = "Your message was received in "
                          + f"{int(self.bot.latency * 1000)}ms.",
            color = discord.Color.green()
        )
        await ctx.send(embed=embedVar)
    
    ### AVATAR ###
    @commands.hybrid_command(
        description = "Get the avatar of any user."
    )
    async def avatar(self, ctx: Context, member: discord.Member = None):
        # Avatar and color information is only accessible using fetch_user()
        target_user = (await self.bot.fetch_user(member.id if member is not None \
                                                 else ctx.author.id))
        avatar_url = target_user.avatar.url
        target_color = target_user.accent_color
        embed_var = discord.Embed(color=target_color)
        embed_var.set_image(url=avatar_url)
        await ctx.send(embed=embed_var)
    
    @avatar.error
    async def avatar_error(self, ctx: Context, error: CommandError):
        if isinstance(error, commands.MemberNotFound):
            embed_var = discord.Embed(
                title = "Member not found",
                description = BAD_MEMBER_MSG,
                color = discord.Color.red()
            )
            await ctx.send(embed=embed_var)
        else:
            await send_generic_error(ctx, error)
    
    ### BANNER ###
    @commands.hybrid_command(
        description = "Get the banner of any user."
    )
    async def banner(self, ctx: Context, member: discord.Member = None):
        # Banner and color information is only accessible using fetch_user()
        target_user = (await self.bot.fetch_user(member.id if member is not None \
                                                 else ctx.author.id))
        banner_url = target_user.banner.url if target_user.banner is not None else None
        target_color = target_user.accent_color
        embed_var = discord.Embed()
        if banner_url is not None:
            embed_var.color = target_color
            embed_var.set_image(url=banner_url)
        else:
            embed_var.title = "This user doesn't have a banner set!"
        await ctx.send(embed=embed_var)
    
    @banner.error
    async def banner_error(self, ctx: Context, error: CommandError):
        if isinstance(error, commands.MemberNotFound):
            embed_var = discord.Embed(
                title = ERROR_TITLE,
                description = BAD_MEMBER_MSG,
                color = discord.Color.red()
            )
            await ctx.send(embed=embed_var)
        else:
            await send_generic_error(ctx, error)

    ### COINFLIP ###
    @commands.hybrid_command(
        description = "Flip a coin!",
        aliases = ["flip", "coin"]
    )
    async def coinflip(self, ctx: Context):
        result = "Heads!" if random.randint(0, 1) == 0 else "Tails!"
        embedVar = discord.Embed(
            title = result,
            description = f"This had a 50% chance of happening.",
            color = discord.Color.green()
        )
        await ctx.send(embed=embedVar)

    ### REPO ###
    @commands.hybrid_command(
        description = "Check out our repository!",
        aliases = ["repository"]
    )
    async def repo(self, ctx: Context):
        embedVar = discord.Embed(
            title = f"Click Here to Redirect to the {self.bot.user.name} Repository!",
            url = "https://github.com/SameriteRL/CARPI-Bot",
            description = "This is a project within the "
                          + "Rensselaer Center for Open Source (RCOS)",
            color = discord.Color.blurple()
        )
        await ctx.send(embed=embedVar)

    ### TEXTBOOKS ###
    @commands.hybrid_command(
        description = "Shhh..."
    )
    async def textbooks(self, ctx: commands.Context):
        drive_link = "https://drive.google.com/drive/folders/1SaiXHIu8-ue2CwCw62ukl0U59KBc26dz"
        embed = discord.Embed(
            title = "Textbook Google Drive",
            description = f"Here is a repository of freely avaliable textbooks. "
                          + "Note that these may or may not be current.",
            url = drive_link,
            color = ctx.author.accent_color
        )
        await ctx.send(embed=embed)
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Miscellaneous(bot))