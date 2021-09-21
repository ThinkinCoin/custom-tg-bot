# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = '1959999716:AAHigsPwdSKo1andiqHhTkUhccwVF7wEFQA'
    OWNER_ID = "1197776016"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "mzfshark"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgresql://makibot:Padrao123#@localhost:5432/makibd'  # needed for any database modules
    MESSAGE_DUMP = ['-1001517742426','-1001245224603']  # needed to make sure 'save from' messages persist
    LOAD = [ ]
    # sed has been disabled after the discovery that certain long-running sed commands maxed out cpu usage
    # and killed the bot. Be careful re-enabling it!
    NO_LOAD = ['rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = [1197776016]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [1197776016]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [1197776016]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 2  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True                                