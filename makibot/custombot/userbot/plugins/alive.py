"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`ππ¦π³π’ ππ° π¦π£ πΆπ¬π² π΄π’π―π’ π±π¬ π‘π¦π’ π±π¬πͺπ¬π―π―π¬π΄. ππ’ππ―π« ππ° π¦π£ πΆπ¬π² π΄π’π―π’ π±π¬ π©π¦π³π’ π£π¬π―π’π³π’π―.πΙͺ α΄α΄ α΄ΚΙͺα΄ α΄ α΄Κ α΄α΄κ±α΄α΄Κππ`**\n\n"
                     "**βTelethon version:- 6.9.0**\nβ β¬β¬β¬β¬β¬β¬ β΄βͺβ΅ β¬β¬β¬β¬β¬β¬ β\n**βPython: 3.7.3**\nβ β¬β¬β¬β¬β¬β¬ β΄βͺβ΅ β¬β¬β¬β¬β¬β¬ β\n"
                     "**βBot Made By:- @Hack12r\nβ β¬β¬β¬β¬β¬β¬ β΄βͺβ΅ β¬β¬β¬β¬β¬β¬ β\n**"
                     "**βDatabase Status: Databases functioning normally!**\nβ β¬β¬β¬β¬β¬β¬ β΄βͺβ΅ β¬β¬β¬β¬β¬β¬ β\nπAlways with you, my peru master!\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     "[Deploy this userbot Now](https://github.com/Hack12R/HardcoreUserbot)")
