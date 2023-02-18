from pyrogram import Client as app
from pyrogram import *
from pyrogram.types import *

@app.on_message(filters.command("start") & filters.private)
async def start_zaen(c: Client, m: Message):
    start_text = f"""
hi {m.from_user.mention}

username: @{m.from_user.username}
userID : {m.from_user.id}

ini tulis 
"""

    await m.reply_text(start_text)
