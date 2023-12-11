import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 8039541))

    API_HASH = os.environ.get("API_HASH", "a33bbdb4aab8726bdc2c73442a0eaeb5")
