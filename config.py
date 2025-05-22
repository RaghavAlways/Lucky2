import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","28954982"))
API_HASH = getenv("API_HASH", "94ccef265a479793912c6691cf4963ea")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7882219337:AAGD8C3LlqTtAZS2Y9ovlL59Cu8k7knlVYM")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Raghav23:Raghav23@cluster0.6nrx6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002430579671))

# Get this value from @purvi_music_bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6502237398))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ifgovtjoftibcdjpvd8nfiokbfobffob0vrb8bd/Heartless-Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private


SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/thanos_network")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/thanos_network")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Get your pyrogram v2 session from @king_string_session_bot on Telegram
STRING1 = getenv("STRING_SESSION", "BQG50WYAa8MpClBGQfbXglJuVaztO4xIl22tGqo-VmDUv-RhvbtqohtgkJCOmE9Rknf8kluKwCsFzmpl2yOnpotF-lD_Vjh5Nz2-WtLAeaDGxRsazDWBt-30Ryoyh9OOF6yynbAMacKOHmrqLGyv0m8eqaVVz-6MswyIFx8C2FcjwXEegwnLtOuj6C9hj0QT2V3a5-u7iqLzDNMvyl_Ya3hOCf1cRoz-09owt23iIjnRjPUG2gtuclprmjLdujzW-dZe5R4ujWCcvp0CD7-MjnxA-647MidJxnHFLPF_bTle2M2WXU_bGZ3NWiMgigi1RotQ9RnCJ5qeBTHtU6CN8WeCmRvtLAAAAAHaLy2nAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/xsvt6b.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://i.ibb.co/tM27hP0x/31eb8a8cb048.png"
)
PLAYLIST_IMG_URL = "https://ibb.co/S4Z3NFdW"
STATS_IMG_URL = "https://ibb.co/S4Z3NFdW"
TELEGRAM_AUDIO_URL = "https://ibb.co/S4Z3NFdW"
TELEGRAM_VIDEO_URL = "https://ibb.co/S4Z3NFdW"
STREAM_IMG_URL = "https://ibb.co/S4Z3NFdW"
SOUNCLOUD_IMG_URL = "https://ibb.co/S4Z3NFdW"
YOUTUBE_IMG_URL = "https://ibb.co/S4Z3NFdW"
SPOTIFY_ARTIST_IMG_URL = "https://ibb.co/S4Z3NFdW"
SPOTIFY_ALBUM_IMG_URL = "https://ibb.co/S4Z3NFdW"
SPOTIFY_PLAYLIST_IMG_URL = "https://ibb.co/S4Z3NFdW"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
