import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Movies update')
API_ID = int(environ.get('API_ID', '25847347'))
API_HASH = environ.get('API_HASH', '11569826ebbc9f8b14c3ab1c5ddb937b')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://media-hosting.imagekit.io//678eb275290f4a9f/4498060.gif?Expires=1834234009&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=YNYC8zmwlddAjEIp7Ma2E4KXqymNnAEB57WvOanxUvNRWGbWaVmtPR3l4jA0srX-jwFmZxVz2bSf8~lKciG-yBPSaRoWQ7pIckqq6X8EqJDuJRojyKeCVYId-7LRHLR1hG0-EA4xuFzcoyku82mwyyMM2Za~aFfMSuNI6mpDbIZk~aCfxmd5XxG0WTl-1MBIiLaIDszfO93-nY24UCC322VY1dcqf3SEh2zYPudJWjEoZFsA~0SJdSJCoG-VQtsW2pr6bxZ7Et-0dZWw5YGFxqAMM7wnoBU7BZi5aIw7jV7sAd5b8i74IDHWDAyV-fro0HQv3M4Vhn~NpHBKEl74eA__ https://media-hosting.imagekit.io//ef667fc393ce4869/8995449.gif?Expires=1834234318&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=nUiR0jaj7bErBBZS7bXQ47f4ZinWfabe3klIxxheu2GQ7wLNQ7ydGDOJPqj34DSqwoFBcjbQgSmZPeQyOQBa-yXa1WsTniwiOSWUQNJvYo-rY91OpSc-JlaXc04ZTF8XptvYjhNcsrJRhSApsoA4sWxTUo~IduDzFS6qr9j1DuxqYeJdHqty7DhN1bH2JOz69FFvBoTDDWMfNQONofezLcoUenw8aCt~hlNLIpOOTihFOWmc6CI83sXLSEHCWdu-xPKkg~AYbIGbuNjADaqqRnyNaXXu6-Aq2F5tThtulDLMFL7mNpALd1DtKftX4ObptgA3yxEj2spkL3Ea2RnmLg__ https://media-hosting.imagekit.io//678eb275290f4a9f/4498060.gif?Expires=1834234009&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=YNYC8zmwlddAjEIp7Ma2E4KXqymNnAEB57WvOanxUvNRWGbWaVmtPR3l4jA0srX-jwFmZxVz2bSf8~lKciG-yBPSaRoWQ7pIckqq6X8EqJDuJRojyKeCVYId-7LRHLR1hG0-EA4xuFzcoyku82mwyyMM2Za~aFfMSuNI6mpDbIZk~aCfxmd5XxG0WTl-1MBIiLaIDszfO93-nY24UCC322VY1dcqf3SEh2zYPudJWjEoZFsA~0SJdSJCoG-VQtsW2pr6bxZ7Et-0dZWw5YGFxqAMM7wnoBU7BZi5aIw7jV7sAd5b8i74IDHWDAyV-fro0HQv3M4Vhn~NpHBKEl74eA__ https://i.imgur.com/1DFSYHy.jpeg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://i.imgur.com/0lN1aa0.jpeg")
MELCOW_VID = environ.get("MELCOW_VID", "https://i.imgur.com/IhB8oCN.jpeg")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/86b7b7e2aa7e38f328902.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://media-hosting.imagekit.io//849409d3b5e34c66/11402995.gif?Expires=1834235077&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=uUCV9aCMKHh2r7VFjJhSFS29m0cRGRn6kwTxxkY3XGN-fawfZJsVu1us2UQSqxehCH9LReW4TICT7DwSszeNq34-jWwn~~ePWHewt9W5EQGbDE2ylKuIzsBjkad7vjKGfJmFPbkBRnnvvN98U7m~AGHqwNtkY7Vna-58fx7qBunhOKs2XAKXLFMUV9wH7DcLCGdyyFrLkdwaAlI0Go0h7g5BzG7WnSroQIimhO--YAwzULzgDSoRmEhzp9UaKyS-06kaRExvvqN~t7BG1pH2jbmUvrmd7HiBKSDcH2xpiZqqNCu-kMywAmYkV0iqYIp5VCv6F0~qZmrgDVQkCNURqg__'))
CODE = (environ.get('CODE', 'https://telegra.ph/file/72f425007b22d28bd935e.jpg'))

#stream link shortner
STREAM_SITE = (environ.get('STREAM_SITE', 'clickspay.in'))
STREAM_API = (environ.get('STREAM_API', '71d6a44224c666d4bae5824828e6d52e17533785'))
STREAMHTO = (environ.get('STREAMHTO', 'https://t.me/codexdisscus'))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5860228893').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002434169448').split()] #Channel id for auto indexing ( make sure bot is admin )
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
auth_channel = environ.get('AUTH_CHANNEL', '-1001747397870') #Channel / Group Id for force sub ( make sure bot is admin )
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002429417244') # support group id ( make sure bot is admin )
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002316461830') # request channel id ( make sure bot is admin )
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False)) # True if you want no results messages in Log Channel

# MongoDB information 
# https://youtu.be/qFB0cFqiyOM?si=QGuFSZ7qhxl4VTrA

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://ap8181568:four@cluster4.ojmga.mongodb.net/?retryWrites=true&w=majority&appName=Cluster4")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster4")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Verify/token system
VERIFY = bool(environ.get('VERIFY', False)) # Verification On ( True ) / Off ( False )
# HOWTOVERIFY = environ.get('HOWTOVERIFY', url='https://t.me/Ultroid_Official/18') 
HOWTOVERIFY = environ.get('HOWTOVERIFY', 'https://t.me/codexdisscus') # How to open tutorial link for verification

# Others
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'clickspay.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '71d6a44224c666d4bae5824828e6d52e17533785')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))  # else--> True
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/codexmoviesgroup')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/codexmoviehere')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/codexdisscus') # Tutorial video link for opening shortlink website 
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : Codexownerr')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001901755533')) #Log channel id ( make sure bot is admin )
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/codexdisscus') #Support group link ( make sure bot is admin )
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002434169448')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), True) #forwoding /sharing
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]

# FQDN = ex. => ttoken-78-cdadf96c95a8.herokuapp.com  (remove 'https://' ttoken-78-cdadf96c95a8.herokuapp.com '/' )

# Online Stream and Download
PORT = int(environ.get('PORT', 8080))
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "http://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)
BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001987654567")).split())) 
OWNER_USERNAME = "Codexownerr"


# add premium logs channel id
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002492785499'))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
