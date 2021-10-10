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


from SophiaBot.events import register
from SophiaBot import telethn as tbot
TMP_DOWNLOAD_DIRECTORY = "./"
from telethon import events
import os
from PIL import Image
from datetime import datetime
from telegraph import Telegraph, upload_file, exceptions
Hero = "SophiaBot"
telegraph = Telegraph()
r = telegraph.create_account(short_name=Hero)
auth_url = r["auth_url"]


@register(pattern="^/t(m|xt) ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    optional_title = event.pattern_match.group(2)
    if event.reply_to_msg_id:
        start = datetime.now()
        r_message = await event.get_reply_message()
        input_str = event.pattern_match.group(1)
        if input_str == "m":
            downloaded_file_name = await tbot.download_media(
                r_message,
                TMP_DOWNLOAD_DIRECTORY
            )
            end = datetime.now()
            ms = (end - start).seconds
            h = await event.reply("Downloaded to {} in {} seconds.".format(downloaded_file_name, ms))
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.now()
                media_urls = upload_file(downloaded_file_name)
            except exceptions.TelegraphException as exc:
                await h.edit("ERROR: " + str(exc))
                os.remove(downloaded_file_name)
            else:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                await h.edit("Uploaded to https://telegra.ph{})".format(media_urls[0]), link_preview=True)
        elif input_str == "xt":
            user_object = await tbot.get_entity(r_message.sender_id)
            title_of_page = user_object.first_name # + " " + user_object.last_name
            # apparently, all Users do not have last_name field
            if optional_title:
                title_of_page = optional_title
            page_content = r_message.message
            if r_message.media:
                if page_content != "":
                    title_of_page = page_content
                downloaded_file_name = await tbot.download_media(
                    r_message,
                    TMP_DOWNLOAD_DIRECTORY
                )
                m_list = None
                with open(downloaded_file_name, "rb") as fd:
                    m_list = fd.readlines()
                for m in m_list:
                    page_content += m.decode("UTF-8") + "\n"
                os.remove(downloaded_file_name)
            page_content = page_content.replace("\n", "<br>")
            response = telegraph.create_page(
                title_of_page,
                html_content=page_content
            )
            end = datetime.now()
            ms = (end - start).seconds
            await event.reply("Pasted to https://telegra.ph/{} in {} seconds.".format(response["path"], ms), link_preview=True)
    else:
        await event.reply("Reply to a message to get a permanent telegra.ph link.")


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


__help__ = """
*Available Commands for Telegraph*

 - /tm :Get Telegraph Link Of Replied Media
 - /txt :Get Telegraph Link of Replied Text
"""

__mod_name__ = "Telegraph"
