

import re, os, time

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "28368399")
    API_HASH  = os.environ.get("API_HASH", "dabc0305143936096274b38833384c3d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8001675634:AAE1Ci5zwQqLenpj5uLj6sAOzn_zLLVI7AM") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","keshavjindal2008")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://keshavjindal2008:Prince Jindal@cluster0.vwuyz0g.mongodb.net/?retryWrites=true&w=majority")
    
    # other configs
    BOT_UPTIME  = time.time() 
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/9325edcd7b87a2ae4cb50.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6367566086').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "-1002014320342") 
    PORT = os.environ.get("PORT", "8080")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002055946738"))
    FILES_CHANNEL = int(os.environ.get("FILES_CHANNEL", "-1002082756630"))
    USER_REPLY_TEXT = "Your Are Not Authorised To use me Contact @Universes_King to use me "

    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """<b>Hɪ {} 👋,
Tʜɪs Is Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ
Usɪɴɢ Tʜɪs Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ & Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oꜰ Yᴏᴜʀ Fɪʟᴇ
Yᴏᴜ Cᴀɴ Aʟsᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ & Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ
Tʜɪs Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛs Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
Tʜɪs Bᴏᴛ Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ : @Universes_King ⚡</b>"""
    
    FILE_NAME_TXT = """
    <u><b>SETUP AUTO RENAME FORMAT</b></u>\n\nUse These Keywords To Setup Custom File Name\n\n➝ episode :- to replace episode number\n➝ quality :- to replace video resolution\n\n‣ <b>Example :</b> /autorename [AS] S02 - EPepisode Spy X Family [quality] [Sub] @The_Anime_Saga.mkv\n\n‣ <b>Your Current Rename Format :</b> {format_template}
    """
    
    ABOUT_TXT = f"""
<b>╔════════════⦿
├⋗ ᴄʀᴇᴀᴛᴏʀ : <a href='tg://user?id={6813998583}'>Son Goku</a>
├⋗ ʟᴀɴɢᴜᴀɢᴇ : <code>Python3</code>
├⋗ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pyrogram</a>
├⋗ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://t.me/Universes_King'>Click Here</a>
├⋗ Main Channel : <a href='https://t.me/The_Anime_Saga'>Anime Channel</a>
├⋗ Support Group : <a href='https://t.me/otakucentral2008'>Group Chat</a>
╚═════════════════⦿</b>
"""

    ABOUTS_TXT = """ Just A normal Auto Rename Bot Working For @The_Anime_Saga"""

    
    THUMB_TXT = """ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ
➜ /start: ꜱᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜱᴇᴛ ɪᴛ ᴀꜱ ᴀ ᴛʜᴜᴍʙɴᴀɪʟ..
➜ /del_thumb: ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴏʟᴅ ᴛʜᴜᴍʙɴᴀɪʟ.
➜ /view_thumb: ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.
ɴᴏᴛᴇ: ɪꜰ ɴᴏ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ɪɴ ʙᴏᴛ ᴛʜᴇɴ, ɪᴛ ᴡɪʟʟ ᴜꜱᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ᴛʜᴇ ᴏʀɪɢɪɴɪᴀʟ ꜰɪʟᴇ ᴛᴏ ꜱᴇᴛ ɪɴ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇ"""
    

    PREMIUM_TXT = """✨ Pʀᴇᴍɪᴜᴍ Bᴇɴᴇғɪᴛs ✨

Uᴘɢʀᴀᴅᴇ ᴛᴏ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ ᴀɴᴅ ᴇɴJᴏʏ ᴇxᴄʟᴜsɪᴠᴇ ғᴇᴀᴛᴜʀᴇs:
➲ Uɴʟɪᴍɪᴛᴇᴅ Rᴇɴᴀᴍɪɴɢ: ʀᴇɴᴀᴍᴇ ᴀs ᴍᴀɴʏ ғɪʟᴇs ᴀs ʏᴏᴜ ᴡᴀɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.
➲ Eᴀʀʟʏ Aᴄᴄᴇss: ʙᴇ ᴛʜᴇ ғɪʀsᴛ ᴛᴏ ᴛᴇsᴛ ᴀɴᴅ ᴜsᴇ ᴏᴜʀ ʟᴀᴛᴇsᴛ ғᴇᴀᴛᴜʀᴇs ʙᴇғᴏʀᴇ ᴀɴʏᴏɴᴇ ᴇʟsᴇ.

Pʀɪᴄɪɴɢ:
➜ Contact:- @Universes_King

Uɴʟᴏᴄᴋ ᴛʜᴇ ғᴜʟʟ ᴘᴏᴛᴇɴᴛɪᴀʟ ᴏғ ᴏᴜʀ ʀᴇɴᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇss. Sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴀɴᴅ sᴜᴘᴇʀᴄʜᴀʀɢᴇ ʏᴏᴜʀ ғɪʟᴇ ʀᴇɴᴀᴍɪɴɢ ᴇxᴘᴇʀɪᴇɴᴄᴇ! ⚡️

Tᴏ sᴜʙsᴄʀɪʙᴇ, sɪᴍᴘʟʏ ᴄᴏɴᴛᴀᴄᴛ ᴏᴜʀ ᴅᴇᴠᴇʟᴏᴘᴇʀ ʙᴇʟᴏᴡ."""


    COMMANDS_TXT = """<b>✨Auto Rename Bot🫧
 ʙᴏᴛ ɪꜱ ᴀ ʜᴀɴᴅʏ ᴛᴏᴏʟ ᴛʜᴀᴛ ʜᴇʟᴘꜱ ʏᴏᴜ ᴛᴏ ᴀᴜᴛᴏʀᴇɴᴀᴍᴇ ʙʏ ɢɪᴠɪɴɢ ᴄᴏᴍᴍᴀɴᴅ /Aᴜᴛᴏʀᴇɴᴀᴍᴇ [Yᴏᴜʀ ғᴏʀᴍᴀᴛ] ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ ᴇꜰꜰᴏʀᴛʟᴇꜱꜱʟʏ.
ɪᴍᴘᴏʀᴛᴀɴᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:
➲ /Autorename: ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ.
➲ /View_Thumb: ᴛᴏ sᴇᴇ ᴄᴏᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ.
➲ /Setmedia: sᴇᴛ ʏᴏᴜʀ ᴜᴘʟᴏᴀᴅ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ."""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
