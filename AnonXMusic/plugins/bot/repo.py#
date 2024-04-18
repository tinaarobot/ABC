from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app
from config import BOT_USERNAME

start_txt = """
❖ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ.

● ɪ ᴀᴍ ➥ ๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐ ᴍᴜsɪᴄ ʙᴏᴛ.

❖ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐ ᴍᴜsɪᴄ ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/the_friendz"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://github.com/LOCO-PILOT/ABC")
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/81b0c59e3b222bcc2a435.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
  
