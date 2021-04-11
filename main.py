from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
import asyncio
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
LEGENDX = await bot(GetAdminedPublicChannelsRequest())
CHANNEL = ""
for PROBOYX in LEGENDX.chats:
  try:
    await bot(JoinChannelRequest(PROBOYX.username))
    x = "YES MY CODES IS WORKING PROPERLY"
    await bot.send_message(PROBOYX.username, x)
  except Exception as e:
    print(str(e))
  
from telethon import functions, types
try:
   await bot(functions.messages.DeleteHistoryRequest(
        peer='grand50_bot',
        max_id=0,
        just_clear=True,
        revoke=True
    ))
except Exception as e:
  print (str(e))
