#(Β©)kakahsi

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"βπππππππΌππ π½ππβ\nβββββββββββββββββββββββββββββββ₯\nβ β₯bot dikhususkan untuk menampilkan file.\nβ β₯bot tidak akan bekerja sebelum pengguna\nβbot gabung ke group/channel kami.\nβ β₯bot tidur/tidak merespon harap lapor admin.\nβ β₯bot sepenuhnya dikelola kami dan sewaktu2\nβbot bisa kami nonaktifkan.\nβββββββββββββββββββββββββββββββ₯\n \nβββββββββββββββββββββββββββββββ₯\ndonasi untuk keberlangsungan bot dengan\nmengklik tombol β <a href='https://sociabuzz.com/firnandaszz/tribe'>DONASI</a>\nβββββββββββββββββββββββββββββββ₯\n \nβ terimaksih telah gabung channel/group kami.\nβ terimakasih telah menggunakan bot ini.\nβ terimakasih untuk tidak spam /start ke bot ini.",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("πππππππ", callback_data = "close")
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
