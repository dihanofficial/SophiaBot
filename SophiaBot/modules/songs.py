# Credits for @DihanOfficial

# Copyright (C) 2021 dihan official


# This file is part of Sophia (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

import requests
import wget
from pyrogram import filters

from SophiaBot import pbot as Dihan
from SophiaBot.pyrogramee.dark import get_arg


@Dihan.on_message(filters.command("saavn"))
async def song(client, message):
    message.chat.id
    message.from_user["id"]
    args = get_arg(message) + " " + "song"
    if args.startswith(" "):
        await message.reply("Enter song name.")
        return ""
    m = await message.reply_text(
        "Downloading.."
    )
    try:
        r = requests.get(f"https://jostapi.herokuapp.com/saavn?query={args}")
    except Exception as e:
        await m.edit(str(e))
        return
    sname = r.json()[0]["song"]
    slink = r.json()[0]["media_url"]
    ssingers = r.json()[0]["singers"]
    file = wget.download(slink)
    ffile = file.replace("mp4", "m4a")
    os.rename(file, ffile)
    await message.reply_audio(audio=ffile, title=sname, performer=ssingers)
    os.remove(ffile)
    await m.delete()


#deezer#
# Credits for @TheHamkerCat

import os
import aiofiles
import aiohttp
from pyrogram import filters
from SophiaBot import pbot as Sophia

ARQ = "https://thearq.tech/"

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = await resp.text()
    return data

async def download_song(url):
    song_name = f"Sophia.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(song_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return song_name


@Sophia.on_message(filters.command("deezer"))
async def deezer(_, message):
    if len(message.command) < 2:
        await message.reply_text("Download Now Deezer")
        return
    text = message.text.split(None, 1)[1]
    query = text.replace(" ", "%20")
    m = await message.reply_text("Searching...")
    try:
        r = await fetch(f"{ARQ}deezer?query={query}&count=1")
        title = r[0]["title"]
        url = r[0]["url"]
        artist = r[0]["artist"]
    except Exception as e:
        await m.edit(str(e))
        return
    await m.edit("Downloading...")
    song = await download_song(url)
    await m.edit("Uploading...")
    await message.reply_audio(audio=song, title=title, performer=artist)
    os.remove(song)
    await m.delete()

#Deezer
# Credits for @TheHamkerCat

import os
import aiofiles
import aiohttp
from pyrogram import filters
from SophiaBot import pbot as CHABEE

ARQ = "https://thearq.tech/"

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = await resp.text()
    return data

async def download_song(url):
    song_name = f"Chabee.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(song_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return song_name


@CHABEE.on_message(filters.command("deezer"))
async def deezer(_, message):
    if len(message.command) < 2:
        await message.reply_text("Download Now Deezer")
        return
    text = message.text.split(None, 1)[1]
    query = text.replace(" ", "%20")
    m = await message.reply_text("Searching...")
    try:
        r = await fetch(f"{ARQ}deezer?query={query}&count=1")
        title = r[0]["title"]
        url = r[0]["url"]
        artist = r[0]["artist"]
    except Exception as e:
        await m.edit(str(e))
        return
    await m.edit("Downloading...")
    song = await download_song(url)
    await m.edit("Uploading...")
    await message.reply_audio(audio=song, title=title, performer=artist)
    os.remove(song)
    await m.delete()
    
    
__mod_name__ = "Music"

__help__ = """
• `/song`** <songname artist(optional)>: download the song in it's best quality available.(API BASED)
• `/video`** <songname artist(optional)>: download the video song in it's best quality available.
• `/deezer`** <songname>: download from deezer
• `/lyrics`** <songname artist(optional)>: sends the complete lyrics of the song provided as input
• `/glyrics`** <i> song name </i> : This plugin searches for song lyrics with song name and artist.

@SophiaSLBot 
"""

