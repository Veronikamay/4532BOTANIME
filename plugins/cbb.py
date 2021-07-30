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
            text = f"📌ℂℍ𝔸ℕℕ𝔼𝕃𝕊 ℙ𝔸ℝ𝕋ℕ𝔼ℝ𝕊📌\n<b>§ 01 : <a href='https://t.me/pikapikacuk44'>Channel</a>\n§ 02 : <a href='https://t.me/Suryapro69'>Channel</a>\n§ 03 : <a href='https://t.me/gudangsyahwat76'>Channel</a>\n§ Twitter : <a href='https://twitter.com/BFROOMS?s=08'>@BFROOMS</a>\n§ Facebook : - \n§ Owner : @K4N3N</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝕄𝔼ℕ𝕌", callback_data = "close")
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
