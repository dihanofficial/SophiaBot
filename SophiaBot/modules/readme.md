# Sophia  Example plugin format

## Basic: Simple Plugins
```python3

from Sophia.decorator import register
from .utils.disable import disableable_dec
from .utils.message import get_args_str

@register(cmds="Hi")
@disableable_dec("Hi")
async def _(message):
    j = "Say Hello There Im Sophia "
    await message.reply(j)
    
__mod_name__ = "Hi"
__help__ = """
<b>Hi</b>
- /hi: Say Hello There Im Sophia 
"""
```

## Basic: Env Vars
```python3
# You can import env like this. If config present auto use config

from Sophia.decorator import register
from .utils.disable import disableable_dec
from .utils.message import get_args_str
from Sophia.config import get_int_key, get_str_key

HI_STRING = get_str_key("HI_STRING", required=True) # String
MULTI = get_int_key("MULTI", required=True) #Intiger

@register(cmds="Hi")
@disableable_dec("Hi")
async def _(message):
    j = HI_STRING*MULTI
    await message.reply(j)
    
__mod_name__ = "Hi"
__help__ = """
<b>Hi</b>
- /hi: Say Hello There Im Sophia 
"""
```



## Advanced: Pyrogram
```python3
from Sophia.pyrogramee.pluginhelpers import admins_only
from Sophia.pyrogramee.pyrogram import pbot

@pbot.on_message(filters.command("hi") & ~filters.edited & ~filters.bot)
@admins_only
async def hmm(client, message):
    j = "Hello there"
    await message.reply(j)
    
__mod_name__ = "Hi"
__help__ = """
<b>Hi</b>
- /hi: Say Hello There Im Sophia 
"""
```

## Advanced: Telethon
```python3

from Sophia.telethon import tbot
from Sophia.events import register

@register(pattern="^/hi$")
async def hmm(event):
    j = "Hello there"
    await event.reply(j)
    
__mod_name__ = "Hi"
__help__ = """
<b>Hi</b>
- /hi: Say Hello There Im Sophia 
"""
```
