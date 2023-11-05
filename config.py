from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "8828ed9ae1e7b1538d04d8a6de85589e")
      API_ID = int(getenv("API_ID", "1789161"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6945663522:AAGn0W9Pguj_13gUbCWyNl-h_YiXgJo-w0s")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1670336143:-2116075401").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
