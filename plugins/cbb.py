#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>𝗕𝗛𝗔𝗥𝗔𝗧𝗛_𝗕𝗢𝗬</a>\n○ Language : <code>𝗣𝗬𝗧𝗛𝗢𝗡 𝟯</code>\n○ Library : <a href='https://docs.pyrogram.org/'>𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝗮𝘀𝘆𝗻𝗰𝗶𝗼 {__version__}</a>\n○ MAIN CHANNEL : <a href='https://t.me/filmztube'>𝗙𝗜𝗟𝗠𝗭 𝗧𝗨𝗕𝗘 ⎚</a>\n○Series Channel : <a href='https://t.me/filmztube'>𝗙𝗜𝗟𝗠𝗭 𝗧𝗨𝗕𝗘 ⎚ [𝗦𝗘𝗥𝗜𝗘𝗦]</a>\n</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
