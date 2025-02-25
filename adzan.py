import json
import requests
from pyrogram import *
from pyrogram.types import *
from PyroUbot import *

__MODULE__ = "ʜᴏsᴛ"
__HELP__ = f"""
<blockquote><b>『 bantuan untuk ʜᴏsᴛ 』</b>

  <b>• perintah:</b> <code>.http</code> [nama kota]
  <b>• penjelasan:</b> Untuk Lihat Info Web</blockquote>
"""

@PY.UBOT("http")
async def adzan(client, message):
    lok = message.text.split(" ", 1)
@PY.UBOT("ping")
async def adzan(client, message):
    lok = message.text.split(" ", 1)