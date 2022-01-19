# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = '5064224906:AAFBOZ6uqVLaFy-CaqeQ6pUJgM6as2zJNfc'
    OWNER_ID = "1197776016"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "mzfshark"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://defightbot:2l6N9JP5@localhost:5432/defight_db'  # needed for any database modules
    MESSAGE_DUMP = ['-1001789233935']  # needed to make sure 'save from' messages persist
    LOAD = [ ]
    # sed has been disabled after the discovery that certain long-running sed commands maxed out cpu usage
    # and killed the bot. Be careful re-enabling it!
    NO_LOAD = ['rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = [1197776016]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = ['1197776016','1747656989','1846761465','1074099080','1387271353']  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = ['1747656989','1846761465','1074099080','1387271353']  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 2  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker..
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True                                
