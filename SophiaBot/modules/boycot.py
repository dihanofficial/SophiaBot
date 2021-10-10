import os

from SophiaBot import pbot
from SophiaBot.pyrogramee.pluginshelper import edit_or_reply
from SophiaBot.pyrogramee.pluginshelper import convert_to_image
from pyrogram import filters
from PIL import Image


@pbot.on_message(filters.command("boycott") & ~filters.edited & ~filters.bot)
async def boycott_kangs(client, message):
    tgi = await edit_or_reply(message, "Applying BoyCott Magic!")
    if not message.reply_to_message:
        await tgi.edit("Please, Reply To Media To Add Boycott Magic!..")
        return
    img = await convert_to_image(message, client)
    if not img:
        await tgi.edit("Reply to a valid media first..")
        return
    if not os.path.exists(img):
        await tgi.edit("`Invalid Media!`")
        return
    background = Image.open(img).convert("RGBA")
    foreground = Image.open("./Sophia/resources/x-cross.png").convert("RGBA")
    x, y = foreground.size
    foreground = foreground.resize(background.size)
    background.paste(foreground, (0, 0), foreground)
    file_name = "bcig.webp"
    background.save(file_name, "WebP")
    if message.reply_to_message:
        await client.send_sticker(
            message.chat.id,
            sticker=file_name,
            reply_to_message_id=message.reply_to_message.message_id,
        )
    else:
        await client.send_sticker(message.chat.id, sticker=file_name)
    await tgi.delete()
    for files in (file_name, img):
        if files and os.path.exists(files):
            os.remove(files)
            

__mod_name__ = "BoyCot Image" 

__help__ = """ 
*BoyCot_Img* - Creates Boycott Image Like this 🙋‍♀️

/boycott (reply to image)

"""

