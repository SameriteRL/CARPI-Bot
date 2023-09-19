import os
import sys
import discord

# Prefix for all bot commands
COMMAND_PREFIX = open("..\CMD_PREFIX.txt").read().strip()
if len(COMMAND_PREFIX) == 0:
    sys.exit(1)

# For use in commands that check for owner status
OWNER_IDS = \
{
    230003732836909056, # Raymond
    208718477240827905, # Julian
    522893218036187138, # Miranda
    810600609736163329, # Florence
    322193892260708352, # Ryan
    298223516262596608, # Anthony
    185164088479973394, # Justin
    534900930915729408 # Lawrence
}

# For use in temporary messages
DEL_DELAY = 3

# For use in error handlers
ERROR_TITLE = "Something went wrong."
NO_PERM_MSG = "You don't have permissions to do that."

async def sendDefaultError(ctx):
    embed_var = discord.Embed(title=ERROR_TITLE,
                             description="Unknown error. Contact an admin for more details.",
                             color=0xC80000)
    embed_var.set_footer(text=f"\u200bCommand attempted by {ctx.author.name}#{ctx.author.discriminator}")
    await ctx.send(embed=embed_var)