from telethon import events
import asyncio
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"marte"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 549755813888)
 

    await event.edit("🔵🔴 🔴🔵")
    animation_chars = [
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",    
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            "`🔴🔵 MARTE PICCOLA KAWAII 🔵🔴`",
            "`🔵🔴 MARTE PICCOLA KAWAII 🔴🔵`",
            ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 549755813888])
