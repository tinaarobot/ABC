from pyrogram import filters
import requests, random
from bs4 import BeautifulSoup
from AnonXMusic import app
import pytgcalls
import os, yt_dlp 
from pyrogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
from pytgcalls.types import AudioVideoPiped
#from AnonXMusic.plugins.play import play
#from AnonXMusic.plugins.play.porndl import play

######

keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close_data"), 
        ]
])

#######
       
@app.on_callback_query(filters.regex("^close_data"))
async def close_callback(_, query):
    chat_id = query.message.chat.id
    await query.message.delete()

########  

def get_video_info(title):
    url_base = f'https://www.xnxx.com/search/{title}'
    try:
        with requests.Session() as s:
            r = s.get(url_base)
            soup = BeautifulSoup(r.text, "html.parser")
            video_list = soup.findAll('div', attrs={'class': 'thumb-block'})
            if video_list:
                random_video = random.choice(video_list)
                thumbnail = random_video.find('div', class_="thumb").find('img').get("src")
                if thumbnail:
                    # Replace the size in the thumbnail URL to get 500x500
                    thumbnail_500 = thumbnail.replace('/h', '/m').replace('/1.jpg', '/3.jpg')
                    link = random_video.find('div', class_="thumb-under").find('a').get("href")
                    if link and 'https://' not in link:  # Check if the link is a valid video link
                        return {'link': 'https://www.xnxx.com' + link, 'thumbnail': thumbnail_500}
    except Exception as e:
        print(f"Error: {e}")
    return None


@app.on_message(filters.command("porn"))
async def get_random_video_info(client, message):
 # if len(message.command) == 1:
       # await message.reply("❖ Please provide a title to search.")
      # return
     
             if message.chat.type != ChatType.PRIVATE:
        return await message.reply("**❍ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ᴜsᴀʙʟᴇ ɪɴ ᴘᴍ ғᴏʀ ɢʀᴏᴜᴘ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ.**",
         reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ɢᴏ ᴘᴍ", url=f"https://t.me/{app.me.username}?start=True")]
           ]
        ))

       # await message.reply("❖ Please provide a title to search.")
        #return

    title = ' '.join(message.command[1:])
    video_info = get_video_info(title)
    
    if video_info:
        video_link = video_info['link']
        video = await get_video_stream(video_link)
        await message.reply_video(video, caption=f"❖ ᴛʜɪs ɪs ʏᴏᴜʀ sᴇᴀʀᴄʜ ➥ {title}", reply_markup=keyboard)
             
    else:
        await message.reply(f"❖ No video link found for ➥ {title}")


