"""
XIT License 2021

Copyright (c) 2021 Dihan Official


"""
import asyncio
import os
import subprocess
import time

import psutil
from pyrogram import filters

from SophiaBot import (bot_start_time, DEV_USERS, pbot)
from SophiaBot.utils import formatter




# Stats Module

async def bot_sys_stats():
    bot_uptime = int(time.time() - bot_start_time)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
root@Thunder GoHelp
------------------
UPTIME: {formatter.get_readable_time((bot_uptime))}
BOT: {round(process.memory_info()[0] / 1024 ** 2)} MB
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%

------------------
"""
    return stats


