from Yukki.config import LOG_GROUP_ID
from Yukki.YukkiUtilities.tgcallsrun import ASS_ACC


async def LOG_CHAT(message, what):
    if message.chat.username:
        chatusername = (f"@{message.chat.username}")
    else:
        chatusername = ("VeezMegaBotChat")
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")" 
    logger_text = f"""
**🚀 New {what}**

**• Chat:** {message.chat.title} 
**• Chat ID:** [`{message.chat.id}`]
**• User:** {mention}
**• Username:** @{message.from_user.username}
**• User ID:** `{message.from_user.id}`
**• Chat Link:** {chatusername}
**• Query:** {message.text}"""
    await app.send_message(LOG_GROUP_ID, 
               text = f"{logger_text}", 
               reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="ᴠɪᴇᴡs​​", url=f"https://t.me/{chatusername}")]]),
               disable_web_page_preview=True,
          )
