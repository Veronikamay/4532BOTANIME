#(©)kakashi

import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from bot import Bot
from config import ADMINS, START_MSG, OWNER_ID, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON
from helper_func import subscribed, encode, decode, get_messages

@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("𝐓𝐔𝐍𝐆𝐆𝐔 𝐒𝐄𝐁𝐄𝐍𝐓𝐀𝐑 ...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("𝐓𝐄𝐑𝐉𝐀𝐃𝐈 𝐊𝐄𝐒𝐀𝐋𝐀𝐇𝐀𝐍 ...")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = 'html', reply_markup = reply_markup)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = 'html', reply_markup = reply_markup)
            except:
                pass
        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝐈𝐍𝐅𝐎 𝐁𝐎𝐓", callback_data = "about"),
                    InlineKeyboardButton("𝐊𝐄𝐌𝐁𝐀𝐋𝐈", callback_data = "close")
                ]
            ]
        )
        await message.reply_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        return

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    text = "<b>Akses Bot ditolak!!\nKamu Harus Join Channels/Groups Kami Sebelum Menggunakan Bot ini.\n1.Silahkan Klik Tombol Gabung Dibawah Untuk Menggunakan Bot ini.\n2.Bila Sudah, Kembali ke bot.\n3.lalu ⇉  </b>"
    message_text = message.text
    try:
        command, argument = message_text.split()
        text = text + f" <b>➡️<a href='https://t.me/{client.username}?start={argument}'>𝐊𝐋𝐈𝐊 𝐓𝐄𝐊𝐒 𝐈𝐍𝐈</a></b>"
    except ValueError:
        pass
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("𝐆𝐀𝐁𝐔𝐍𝐆", url = client.invitelink)]])
    await message.reply(
        text = text,
        reply_markup = reply_markup,
        quote = True,
        disable_web_page_preview = True
    )
