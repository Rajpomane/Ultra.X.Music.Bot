

from Deepak.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
    EMOJI,    
)
 

def stream_markup(user_id):
  buttons = [  
            [                         
            InlineKeyboardButton(text="• ɱəɳʉ •", callback_data=f'cbmenu | {user_id}'),
            InlineKeyboardButton(text="• Cʟᴏsᴇ •", callback_data=f'cls'),
            ],
            ]
  return buttons







@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n

Aʟʟᴏᴡs Yᴏᴜ Tᴏ Pʟᴀʏ Mᴜsɪᴄ Aɴᴅ Vɪᴅᴇᴏ Oɴ Gʀᴏᴜᴘs**""",
        reply_markup=InlineKeyboardMarkup(
            [                                
            [
                    InlineKeyboardButton("📚 Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("👤 Owner", url=f"https://t.me/{OWNER_NAME}"),
            ],
            [
                    InlineKeyboardButton(
                          "✚ Add me to your Group ✚",
                          url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    ),                   
                ],
                [
                    InlineKeyboardButton(
                        "📨 Support", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📨 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],                
                [
                    InlineKeyboardButton(
                        "🌐 Source Code", url="https://github.com/OFFICIALHACKERERA"
                    )
                ],
            ]
        ),        
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sudo Cmd", callback_data="cbsudo"),
                ],
                [
                    InlineKeyboardButton("Users Commands", callback_data="cbbasic")                                    
                       
                ],
                [

                InlineKeyboardButton("Sᴘᴀᴍ Mᴇɴᴜ", callback_data="spam_menu"),
                InlineKeyboardButton("Cʜᴀᴛ Bᴏᴛ", callback_data="chatbot"),
                ],                
                [
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the basic commands:

{EMOJI} /play (song name/link) - play music on video chat
{EMOJI} /vplay (video name/link) - play video on video chat
{EMOJI} /vstream - play live video from yt live/m3u8
{EMOJI} /playlist - show you the playlist
{EMOJI} /video (query) - download video from youtube
{EMOJI} /song (query) - download song from youtube
{EMOJI} /lyric (query) - scrap the song lyric
{EMOJI} /search (query) - search a youtube video link

{EMOJI} /ping - show the bot ping status
{EMOJI} /uptime - show the bot uptime status
{EMOJI} /alive - show the bot alive info (in group)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the admin commands:

{EMOJI} /pause - pause the stream
{EMOJI} /resume - resume the stream
{EMOJI} /skip - switch to next stream
{EMOJI} /stop - stop the streaming
{EMOJI} /vmute - mute the userbot on voice chat
{EMOJI} /vunmute - unmute the userbot on voice chat
{EMOJI} /volume `1-200` - adjust the volume of music (userbot must be admin)
{EMOJI} /reload - reload bot and refresh the admin data
{EMOJI} /userbotjoin - invite the userbot to join group
{EMOJI} /userbotleave - order userbot to leave from group

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

{EMOJI} /rmw - clean all raw files
{EMOJI} /rmd - clean all downloaded files
{EMOJI} /info - show the system information
{EMOJI} /update - update your bot to latest version
{EMOJI} /restart - restart your bot
{EMOJI} /leaveall - order userbot to leave from all group

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )



@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("▢", callback_data="cbstop"),
                      InlineKeyboardButton("II", callback_data="cbpause"),
                      InlineKeyboardButton("▷", callback_data="cbresume"),
                      InlineKeyboardButton(text="‣‣I", callback_data=f"set_skip"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()






@Client.on_callback_query(filters.regex("spam_menu"))
async def spam_menu(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Spam", callback_data="spam"),
                    InlineKeyboardButton("Raid", callback_data="raid"),
                ],
                [
                    
                    InlineKeyboardButton("Vc Raid", callback_data="VcRaid"),
                ],                                                    
                [
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("spam"))
async def spam(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

{EMOJI} /spam - count message to spam
{EMOJI} /bigspam - count message to spam
{EMOJI} /delayspam - sleep time> count reply to a message
{EMOJI} /pornspam - count <message to spam

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="spam_menu")]]
        ),
    )

@Client.on_callback_query(filters.regex("raid"))
async def raid(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

{EMOJI} /raid  count Username of User
{EMOJI} /replyraid  reply to a User.
{EMOJI} /dreplyraid reply to a User

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="spam_menu")]]
        ),
    )


@Client.on_callback_query(filters.regex("VcRaid"))
async def VcRaid(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

{EMOJI} /vcraid <chatid> - Give a Chat Id Else Username To Voice Raid.
{EMOJI} /vraid <chatid + Reply To Video File> - To Raid Video.
{EMOJI} /raidpause - To Pause Raid.
{EMOJI} /raidresume To Resume Raid.
{EMOJI} /raidend <chatid> To End Audio/Video Raid.
⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="spam_menu")]]
        ),
    )

@Client.on_callback_query(filters.regex("chatbot"))
async def chatbot(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""chatbot commands:

{EMOJI} Usage: /chatbot [on|off] only group

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )



