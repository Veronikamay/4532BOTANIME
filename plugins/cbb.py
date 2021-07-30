#(©)kakahsi

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"𝙄𝙉𝙁𝙊𝙍𝙈𝘼𝙎𝙄 𝘽𝙊𝙏 𝘼𝘿𝘼 𝘿𝙄 𝘽𝙄𝙊 𝘽𝙊𝙏",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝐊𝐄𝐌𝐁𝐀𝐋𝐈", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
