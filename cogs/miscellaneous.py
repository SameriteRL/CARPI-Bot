import discord
from discord.ext import commands
from globals import *
import random
import datetime

class Miscellaneous(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ### PING ###
    @commands.command(description="Gets the latency of the server")
    async def ping(self, ctx):
        # Retrieves the server latency in milliseconds
        embedVar = discord.Embed(title="Pong!", description=f"Your message was recieved in {round(self.bot.latency * 1000)}ms.", color=0x00C500, timestamp=datetime.datetime.now())
        embedVar.set_footer(text=f"\u200bPing checked by {ctx.author.nick}")
        await ctx.send(embed=embedVar)
    
    @ping.error
    async def ping_error(self, ctx, error):
        # Should never run. If this runs then bruh
        if isinstance(error, commands.BadArgument):
            await ctx.send("Something went wrong.")
    
    ### AVATAR ###
    @commands.command(description="Gets the avatar of any user")
    async def avatar(self, ctx, member:discord.Member=None):
        if (member == None):
            await ctx.send(ctx.author.display_avatar)
        else:
            await ctx.send(member.display_avatar)
    
    @avatar.error
    async def avatar_error(self, ctx, error):
        # Should never run. If this runs then bruh
        if isinstance(error, commands.BadArgument):
            await ctx.send("Something went wrong.")
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Invalid member.")

    ### COINFLIP ###
    @commands.command(description="Flips a coin. Can either be heads or tails.", aliases=["flip", "coin"])
    async def coinflip(self, ctx):
        # Calls a random float between 0 and 0.99 inclusive. Returns heads if 0 - 0.48 and tails if 0.49 - 0.99
        result = "Heads!" if random.randint(0, 1) == 0 else "Tails!"
        embedVar = discord.Embed(title="Coin Flip Result", description=f"{result}", color=0x00C500, timestamp=datetime.datetime.now())
        embedVar.set_footer(text=f"\u200bCoin flipped by {ctx.author.nick}")
        await ctx.send(embed=embedVar)
    
    @coinflip.error
    async def coinflip_error(self, ctx, error):
        # Should never run. If this runs then bruh
        if isinstance(error, commands.BadArgument):
            await ctx.send("Something went wrong.")

    ### REPO ###
    @commands.command(description="Returns a message that can be interacted with (clicked on) bringing a user to our GitHub Repo.")
    async def repo(self, ctx):
        embedVar = discord.Embed(title=f"Click Here to Redirect to the {ctx.guild.get_member(1067560443444478034).name} Repository", url='https://github.com/Zen1124/tsdb', color=0x0099FF, timestamp=datetime.datetime.now())
        embedVar.set_footer(text=f"\u200bRepository link requested by {ctx.author.nick}")
        await ctx.send(embed=embedVar)
    
    @repo.error
    async def repo_error(self, ctx, error):
        # Should never run. If this runs then bruh
        if isinstance(error, commands.BadArgument):
            await ctx.send("Something went wrong.")
    
    @commands.hybrid_command(description="Sends a link that can be used to invite CARPI to a server, or invite a user to a channel.")
    async def invite(self, ctx, *, args:str=""):
        # embedVar = discord.Embed(title="Click Here to Redirect to the {} Repository".format(ctx.guild.get_member(1067560443444478034).name), url='https://github.com/Zen1124/tsdb', color=0x0099FF, timestamp=datetime.datetime.now())

        if len(args) == 0:
            embedVar = discord.Embed(title=f"Click Here To Add {ctx.guild.get_member(1067560443444478034).name} To a Server", url='https://discord.com/api/oauth2/authorize?client_id=1067560443444478034&permissions=8&scope=bot', color=0x0099FF, timestamp=datetime.datetime.now())
            embedVar.set_footer(text=f"\u200bBot invite link requested by {ctx.author.nick}")
            await ctx.send(embed= embedVar)

        elif len(args) == 1:
            if args[0] == 'vc':
                if ctx.author.voice == None:
                    embedVar = discord.Embed(title="Voice Channel Invite Failed", description="You must be in a voice channel to get a valid invite link.", color=0xC80000, timestamp=datetime.datetime.now())
                    embedVar.set_footer(text=f"\u200bVoice chat invite requested by {ctx.author.nick}")
                    await ctx.send(embed= embedVar)
                else:
                    await ctx.send(await ctx.author.voice.channel.create_invite(max_age = 300) )
            
            elif args[0] == 'here':
                await ctx.send(await ctx.channel.create_invite(max_age = 300) )
        
        else:
            await ctx.send(f"Usage: `{COMMAND_PREFIX}invite [optional \"vc\"]`")
    
    @invite.error
    async def invite_error(self, ctx, *args:str, error):
        # Should never run. If this runs then bruh
        if isinstance(error, commands.BadArgument):
            await ctx.send("Something went wrong.")
        elif len(args) == 1 and args[0] == 'vc' and ctx.author.voice == None:
            embedVar = discord.Embed(title="Voice Channel Invite Failed", color=0xC80000, timestamp=datetime.datetime.now())
            embedVar.set_footer(text=f"\u200bVoice chat invite requested by {ctx.author.nick}")
            await ctx.send(embed= embedVar)
    
    ### SECRET MESSAGE ###
    @commands.command(description="Secretly message someone")
    async def secretmessage(self, ctx, members: commands.Greedy[discord.Member], *, msg="Hey!"):
        for x in members:
            if not x.dm_channel == None:
                await x.dm_channel.send(f"Secret message: {msg}")
                await ctx.send("Message sent!")
            else:
                await x.create_dm()
                await x.dm_channel.send(f"Secret message: {msg}")
                await ctx.send("Message sent!")
        await ctx.message.delete()

    ### get the role
    @commands.command(description="gets the roles the specific users have")
    async def getRole(self, ctx, members: commands.Greedy[discord.Member]):
        for i in members:
            await ctx.send(f"User: {i}")
            await ctx.send(f"roles: {i.top_role}")

    ## CUURENTLY WORK IN PROGRESS
    ### blackjack game
    @commands.command(description = "blackjack game")
    async def blackJack(self, ctx, msg:bool):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        currentnum = random.choice(nums)
        statement = msg
        await ctx.send(currentnum)
        while (currentnum <= 21 and statement == True):
            currentnum += random.choice(nums)
            await ctx.send(currentnum)

    @blackJack.error
    async def blackJack(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("incorrrect input value, must be a bool")

async def setup(bot):
    await bot.add_cog(Miscellaneous(bot))