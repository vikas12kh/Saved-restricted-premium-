# devgaganin
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22694914"))
API_HASH = getenv("API_HASH", "4fd02c02368941a03d48ecab3a3b4a31")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "7491374623"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://parojet681:2n3s5tMUZou9xIOI@cluster0.hvai6mm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", ""))
FORCESUB = getenv("FORCESUB", "")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "") # this is jkust to help if you dont want to force your bot user to login or if they not interested

