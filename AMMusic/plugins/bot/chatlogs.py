import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import LOG, LOGS
from AMMusic import app  

photo = [
    "https://telegra.ph/file/0c87c715c94cee2322a4b.jpg",
    "https://telegra.ph/file/7483763c4d8dc3f2720cb.jpg",
    "https://telegra.ph/file/4500be253b16522c8d8f1.jpg",
    "https://telegra.ph/file/fbe8a40e9ee3741b3be2d.jpg",
    "https://telegra.ph/file/1eb67c100ff8029ae585a.jpg",
    "https://telegra.ph/file/329af57b84f7c76f997ef.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            username = message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
            msg = (
                f"**📝ꜱʜɪᴢᴜᴋᴀ 乂 ᴍᴜꜱɪᴄ 𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ**\n\n"
                f"**📌𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n"
                f"**🍂𝐂ʜᴀᴛ 𝐈ᴅ:** {message.chat.id}\n"
                f"**🔐𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ:** @{username}\n"
                f"**📈𝐆ʀᴏᴜᴘ 𝐌ᴇᴍʙᴇʀs:** {count}\n"
                f"**🤔𝐀ᴅᴅᴇᴅ 𝐁ʏ:** {message.from_user.mention}\n"
            )
            await app.send_photo(LOGS, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"**✫** <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> **✫**\n\n**𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ :** {title}\n\n**𝐂ʜᴀᴛ 𝐈ᴅ :** {chat_id}\n\n**𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ :** {remove_by}\n\n**𝐁ᴏᴛ : @{app.username}\n"
        await app.send_photo(LOGS, photo=random.choice(photo), caption=left)
