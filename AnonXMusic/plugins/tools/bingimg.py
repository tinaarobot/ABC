import json

import requests
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, Message
from AnonXMusic import app


@app.on_message(filters.command("bingimg"))
async def bingimg_search(client: Client, message: Message):
    try:
        text = message.text.split(None, 1)[
            1
        ]  # Extract the query from command arguments
    except IndexError:
        return await message.reply_text(
            "❍ ᴘʀᴏᴠɪᴅᴇ ᴍᴇ ᴀ ǫᴜᴇʀʏ ᴛᴏ sᴇᴀʀᴄʜ!"
        )  # Return error if no query is provided

    search_message = await message.reply_text(
        "💫"
    )  # Display searching message

    # Send request to Bing image search API
    url = "https://sugoi-api.vercel.app/bingimg?keyword=" + text
    resp = requests.get(url)
    images = json.loads(resp.text)  # Parse the response JSON into a list of image URLs

    media = []
    count = 0
    for img in images:
        if count == 7:
            break

        # Create InputMediaPhoto object for each image URL
        media.append(InputMediaPhoto(media=img))
        count += 1

    # Send the media group as a reply to the user
    await message.reply_media_group(media=media)

    # Delete the searching message and the original command message
    await search_message.delete()
    await message.delete()
  
