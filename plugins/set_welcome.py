import asyncio
from info import ADMINS
from pyrogram import Client as Mr_bots, filters



@Mr_bots.on_message((filters.private | filters.group) & filters.command('setwelcome'), group=8)
async def setwelcome(client, message):
    sts = await message.reply("β³οΈ")
    await asyncio.sleep(0.3)
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f" ππΎππ π°ππ΄ π°π½πΎπ½ππΌπΎππ π°π³πΌπΈπ½. /connect {message.chat.id} πΈπ½ πΏπΌ")
    chat_type = message.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("πΌπ°πΊπ΄ ππππ΄ πΈπ°πΌ πΏππ΄ππ΄π½π πΈπ½ ππΎππ πΆππΎππΏ..!", quote=True)
                return
        else:
            await message.reply_text("πΈπ°πΌ π½πΎπ π²πΎπ½π½π΄π²ππ΄π³ π°π½π πΆππΎππΏ..!", quote=True)
            return

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    member = await client.get_chat_member(grp_id, userid)
    if (member.status != enums.ChatMemberStatus.ADMINISTRATOR and member.status != enums.ChatMemberStatus.OWNER and userid not in ADMINS):
        return

    if len(message.command) < 2:
        return await sts.edit("π·πΎπ ππΎ πππ΄ ππ·πΈπ π²πΎπΌπΌπ°π½π³..!", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π²π»πΈπ²πΊ π·π΄ππ΄", callback_data="welcome") ]] ))

    pr0fess0r_99 = message.text.split(" ", 1)[1]
    await save_group_settings(grp_id, 'welcometext', pr0fess0r_99)
    await sts.edit(f"""πππ²π²π΄πππ΅ππ»π»π π²π·π°π½πΆπ΄π³ ππ΄π»π²πΎπΌπ΄ πΌπ΄πππ°πΆπ΄ π΅πΎπ {title} ππΎ\n\n{pr0fess0r_99}""", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("Γ π²π»πΎππ΄ Γ", callback_data="close") ]] ))
