from YukkiMusic import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MUSIC_BOT_NAME as BOT_NAME

BOT_USERNAME = app.username
START_TEXT = f"""
β¨ **Hello MENTION !**

"""

COMMANDS_TEXT = f"""
β¨ **Hello MENTION !**

**πΚΙͺα΄α΄ πΙ΄ πΚα΄ πα΄α΄α΄α΄Ι΄s πα΄Κα΄α΄‘ πα΄ πΙ΄α΄α΄‘ πΚ πα΄α΄α΄α΄Ι΄α΄s.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="β‘ Cα΄α΄α΄α΄Ι΄α΄s", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="π§ Sα΄α΄α΄ΙͺΙ΄Ι’s", callback_data="settings_helper"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="πα΄α΄ α΄α΄", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),                       
        ],        
    ]
)

COMMANDS_BUTTON_USER = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="πα΄α΄ΙͺΙ΄ πα΄α΄α΄α΄Ι΄α΄s", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="πα΄α΄ πα΄α΄α΄α΄Ι΄α΄s", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="πΚα΄Κ πα΄α΄s", callback_data="play_cmd"
            ),            
            InlineKeyboardButton(
                text="β πxα΄Κα΄ β", url="https://telegra.ph/π©πͺ-π©π°π΅π­π¬πΉπ΅πΌπ΄πͺπ©π―ππ―π―ππͺ-08-28"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="β", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="β πΚα΄sα΄ β", callback_data="close_btn"
            ),            
        ],                
    ]
)

COMMANDS_BUTTON_SUDO = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="πα΄α΄ΙͺΙ΄ πα΄α΄α΄α΄Ι΄α΄s", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="πα΄α΄ πα΄α΄α΄α΄Ι΄α΄s", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="πΚα΄Κ πα΄α΄α΄α΄Ι΄α΄s", callback_data="play_cmd"
            ),
            InlineKeyboardButton(
                text="πα΄α΄α΄ πα΄α΄α΄α΄Ι΄α΄s", url="https://telegra.ph/πΚα΄-πα΄Κα΄s-08-28-2"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="πxα΄Κα΄ πα΄α΄α΄α΄Ι΄α΄s", url="https://telegra.ph/π©πͺ-π©π°π΅π­π¬πΉπ΅πΌπ΄πͺπ©π―ππ―π―ππͺ-08-28"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="β", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="β πΚα΄sα΄ β", callback_data="close_btn"
            ),            
        ],                
    ]
)

BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="β", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="β πΚα΄sα΄ β", callback_data="close_btn"
            ),            
        ],                        
    ]
)

SUDO_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Sudo Commands", url="https://telegra.ph/πΚα΄-πα΄Κα΄s-08-28-2"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="β", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="β πΚα΄sα΄ β", callback_data="close_btn"
            ),            
        ],                        
    ]
)


ADMIN_TEXT = f"""
β--**Admin Commands:**--

α΄ sα΄α΄Ι΄α΄s ?α΄Κ α΄Κα΄Ι΄Ι΄α΄Κ α΄Κα΄Κ.

/pause α΄Κ /cpause - Pα΄α΄sα΄ α΄Κα΄ α΄Κα΄ΚΙͺΙ΄Ι’ α΄α΄sΙͺα΄.
/resume α΄Κ /cresume- Rα΄sα΄α΄α΄ α΄Κα΄ α΄α΄α΄sα΄α΄ α΄α΄sΙͺα΄.
/mute α΄Κ /cmute- Mα΄α΄α΄ α΄Κα΄ α΄Κα΄ΚΙͺΙ΄Ι’ α΄α΄sΙͺα΄.
/unmute α΄Κ /cunmute- UΙ΄α΄α΄α΄α΄ α΄Κα΄ α΄α΄α΄α΄α΄ α΄α΄sΙͺα΄.
/skip α΄Κ /cskip- Sα΄Ιͺα΄ α΄Κα΄ α΄α΄ΚΚα΄Ι΄α΄ α΄Κα΄ΚΙͺΙ΄Ι’ α΄α΄sΙͺα΄.
/stop α΄Κ /cstop- Sα΄α΄α΄ α΄Κα΄ α΄Κα΄ΚΙͺΙ΄Ι’ α΄α΄sΙͺα΄.
/shuffel α΄Κ /cshuffel- Rα΄Ι΄α΄α΄α΄ΚΚ sΚα΄??Κα΄s α΄Κα΄ α΄Μ¨α΄α΄α΄α΄α΄ α΄Κα΄ΚΚΙͺsα΄.

β--**Specific Skip:**--
/skip or /cskip [Number(example: 3)] 
    - Skips music to a the specified queued number. Example: /skip 3 will skip music to third queued music and will ignore 1 and 2 music in queue.

β--**Loop Play:**--
/loop or /cloop [enable/disable] or [Numbers between 1-10] 
    - When activated, bot loops the current playing music to 1-10 times on voice chat. Default to 10 times.

"""
AUTH_TEXT = """
β--**Auth Users:**--
Auth Users can use admin commands without admin rights in your chat.

/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group.
/authusers - Check AUTH LIST of the group.
"""

AUTH_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="β€ πα΄α΄α΄ β€", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="β πΚα΄sα΄ β", callback_data="close_btn"
            ),            
        ],                        
    ]
)

BOT_TEXT = """
β--**Bot Commands:**--

/stats - Get Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat etc etc.

/sudolist - Check Sudo Users of Yukki Music Bot

/lyrics [Music Name] - Searches Lyrics for the particular Music on web.

/song [Track Name] or [YT Link] - Download any track from youtube in mp3 or mp4 formats.

c stands for channel play.
/queue or /cqueue- Check Queue List of Music.
"""

PLAY_TEXT = """
β--**Play Commands:**--

Available Commands = play , vplay , cplay

ForcePlay Commands = playforce , vplayforce , cplayforce

c stands for channel play.
v stands for video play.
force stands for force play.

/play or /vplay or /cplay  - Bot will start playing your given query on voice chat or Stream live links on voice chats.

/playforce or /vplayforce or /cplayforce -  Force Play stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.

/channelplay [Chat username or id] or [Disable] - Connect channel to a group and stream music on channel's voice chat from your group.


β--**Bot's Server Playlists:**--
/playlist  - Check Your Saved Playlist On Servers.
/deleteplaylist - Delete any saved music in your playlist
/play  - Start playing Your Saved Playlist from Servers.
"""


BASIC_TEXT = """
π  **Basic Commands:**

/start - Start the bot

/help - Get help message

/play - Play songs or videos in vc

/vplay - Play video in VC

/settings - Check Settings of bot in your group

**Some Useful Commands :** 

/pause /resume /skip /end /loop /shuffle
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="β€ πα΄α΄α΄ β€", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="β πΚα΄sα΄ β", callback_data="close_btn"
            ),            
        ],                        
    ]
)

ADMIN_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="πα΄α΄Κ Cα΄α΄α΄α΄Ι΄α΄s", callback_data="auth_cmds"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="β€ πα΄α΄α΄ β€", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="β πΚα΄sα΄ β", callback_data="close_btn"
            ),            
        ],                        
    ]
)

COMMAND_MENU_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="β πα΄sΙͺα΄ πα΄α΄α΄α΄Ι΄α΄s", callback_data="basic_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="ββπ πα΄α΄ α΄Ι΄α΄α΄α΄ πα΄α΄α΄α΄Ι΄α΄s", callback_data="advanced_cmd"
            ),
        ],
        [
            InlineKeyboardButton(
                text="β€ πα΄α΄α΄ β€", callback_data="open_start_menu"
            ),
            InlineKeyboardButton(
                text="β πΚα΄sα΄ β", callback_data="close_btn"
            ),            
        ],                        
    ]
)
