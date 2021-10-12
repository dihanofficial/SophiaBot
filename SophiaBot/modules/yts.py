import logging

from pyrogram.types import Message
from search_engine_parser import GoogleSearch
from youtube_search import YoutubeSearch

from pyrogram import Client as app, filters

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import pyrogram

logging.getLogger("pyrogram").setLevel(logging.WARNING)

@app.on_message(pyrogram.filters.command("yts"))
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("/yts `YouTube Video Name`")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("Searching....")
        results = YoutubeSearch(query, max_results=6).to_dict()
        i = 0
        text = ""
        while i < 6:
            text += f"Title 🎩 - {results[i]['title']}\n"
            text += f"Duration 🕔 - {results[i]['duration']}\n"
            text += f"Views 👀 - {results[i]['views']}\n"
            text += f"Channel 📺 - {results[i]['channel']}\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
        
@app.on_message(pyrogram.filters.command(["ytsearch"]))
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("/ytsearch `YouTube Video Name`")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("Searching....")
        results = YoutubeSearch(query, max_results=8).to_dict()
        i = 0
        text = ""
        while i < 8:
            text += f"Title 🎩 - {results[i]['title']}\n"
            text += f"Duration 🕔 - {results[i]['duration']}\n"
            text += f"Views 👀 - {results[i]['views']}\n"
            text += f"Channel 📺 - {results[i]['channel']}\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))    
        
  

__mod_name__ = "YouTube"

__help__ = """
=>> *Youtube Video Searching *
 - /yts `Video name` :  To Search In Youtube Until Max Result Is 4
 - /ytsesrch `Video name` :  To Search In Youtube Until Max Result Is 8
"""       
