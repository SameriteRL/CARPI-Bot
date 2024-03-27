import json
import logging
import sys

import discord
from discord.ext.commands import CommandError, Context


async def send_generic_error(ctx: Context, error: CommandError = None) -> None:
    """
    Standard error message for any unhandled or unexpected command errors.
    """
    embed_var = discord.Embed(
        title = ERROR_TITLE,
        description = "Unknown error. Contact an admin for more details.",
        color = 0xC80000
    )
    await ctx.send(embed=embed_var)
    if error is not None:
        logging.error(
            msg = f'Error from command "{ctx.command}" in extension'
                  + f'"{ctx.cog.qualified_name}"',
            exc_info = True
        )

# For use in commands that check for owner status
OWNER_IDS = {
    230003732836909056, # Raymond
    298223516262596608, # Anthony
    310864184923652107, # Edwin
    455125448884748308, # Jack
}

try:
    with open("config.json", "r") as infile:
        CONFIG = json.load(infile)
except:
    print("Bad or missing config.json!")
    sys.exit(1)

# For use in error handlers
ERROR_TITLE = "Something went wrong"
NO_PERM_MSG = "You don't have permissions to do that."
BAD_MEMBER_MSG = "Member not found. Nicknames and usernames are case sensitive, or" \
                 + "maybe you spelled it wrong?"