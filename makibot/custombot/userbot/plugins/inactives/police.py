"""Emoji

Available Commands:

.police

if u edit it then u r gay"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd



@borg.on(admin_cmd(pattern=r"(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

    input_str = event.pattern_match.group(1)

    if input_str == "police":

        await event.edit(input_str)

        animation_chars = [
        
            "š“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ",
            "šµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“",
            "š“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ",
            "šµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“",
            "š“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ",    
            "šµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“",
            "š“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ",
            "šµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“",
            "š“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ",
            "šµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“",
            "š“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ",
            "@Hack12r **Police iz Here**"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
