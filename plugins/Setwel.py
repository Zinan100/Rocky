from pyrogram import Client as Mr_bots, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@Mr_bots.on_message(filters.command('setwelcome'))
async def welcome(bot: Messages, chat_id=id)
    if reply nothing:
        await bot reply_text(
            text="nothing provided for welcome"
        )
    else:
        welcome = message.reply_to_message.text
        await bot.reply_text(
            text=f"youre welcome message saved {title} is {welcome}"
        )
