from YukkiMusic import app
from pyrogram import filters
from YukkiMusic.utils.database.memorydatabase import (get_active_chats, get_active_video_chats)
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.cmdforac import avoice

#Imported Modules

#-------------------------------------------------------------------#

ac_audio = get_active_chats
ac_video = get_active_video_chats




#--------------------------Code------------------#

@app.on_message(avoice(["/ac"]) & SUDOERS)
async def start(client: Client, message: Message):
    await message.reply_text(f"𝗕𝗼𝘁 𝗔𝗰𝘁𝗶𝘃𝗲 𝗖𝗵𝗮𝘁𝘀 𝗜𝗻𝗳𝗼 • 📟\n•━━━━━━━━━━━━━━━━━━•\n🎙•Aᴜᴅɪᴏ  » {ac_audio} Gʀᴏᴜᴘs\n•───────•\n🖥• Vɪᴅᴇᴏ » {ac_video} Gʀᴏᴜᴘs\n•──────•", quote=True)
