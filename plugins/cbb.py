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
            text = f"⎝𝙄𝙉𝙁𝙊𝙍𝙈𝘼𝙎𝙄 𝘽𝙊𝙏⎞\n╔═════════════════════════════✥\n╠✥bot dikhususkan untuk menampilkan file.\n╠✥bot tidak akan bekerja sebelum pengguna\n║bot gabung ke group/channel kami.\n╠✥bot tidur/tidak merespon harap lapor admin.\n╠✥bot sepenuhnya dikelola kami dan sewaktu2\n║bot bisa kami nonaktifkan.\n╚═════════════════════════════✥\n \n╔═════════════════════════════✥\ndonasi untuk keberlangsungan bot dengan\nmengklik tombol ⇉ <a href='https://semawur.com/g5rMPA'>DONASI</a>\n╚═════════════════════════════✥\n \n⚘ terimaksih telah gabung channel/group kami.\n⚘ terimakasih telah menggunakan bot ini.\n⚘ terimakasih untuk tidak spam /start ke bot ini.",
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
