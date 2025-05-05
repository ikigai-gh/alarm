import configparser as cp
import enum
import logging
import os
import sys

from telethon import TelegramClient, events

class MessagePatterns(enum.Enum):
    ROCKET_ALARM = "ракетная опасность"
    ROCKET_ALARM_END = "отбой ракетной опасности"

ENV = os.environ.get("ENV", "PROD")
CONFIG_PATH = "config.ini" if ENV == "PROD" else "config_dev.ini"

logging.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s", level=logging.INFO)
logger = logging.getLogger("alarm")

def read_config():
    try:
        config = cp.ConfigParser()
        config.read(CONFIG_PATH)
        return config
    except FileNotFoundError:
        logger.error(f"Config file not found: {file_path}")
        sys.exit(1)

config = read_config()

logger.info(f"Starting in {ENV}")
logger.info(f"Using {CONFIG_PATH} config file")
logger.info(f"Watching channel id: {config['default']['channel']}")
logger.info(f"Replying with {config['default']['alarm_msg']} and {config['default']['alarm_end_msg']}")
logger.info(f"Forwarding messages to: {config['default']['receipient_id']}")

client = TelegramClient(config['default']["identity"], config['default']["api_id"], config['default']["api_hash"])

@client.on(events.NewMessage(chats=(config['default']["channel"], ), pattern=lambda msg: MessagePatterns.ROCKET_ALARM.value in msg))
async def rocket_alarm(event):
    logger.info(f"Received post that match pattern {MessagePatterns.ROCKET_ALARM} from {config['default']['channel']}")
    await client.send_message(config["default"]["receipient_id"], config["default"]["alarm_msg"])

@client.on(events.NewMessage(chats=(config["default"]["channel"], ), pattern=lambda msg: MessagePatterns.ROCKET_ALARM_END.value in msg))
async def rocket_alarm_end(event):
    logger.info(f"Received post that match pattern {MessagePatterns.ROCKET_ALARM_END} from {config['default']['channel']}")
    await client.send_message(config["default"]["receipient_id"], config["default"]["alarm_end_msg"])

client.start()
client.run_until_disconnected()
