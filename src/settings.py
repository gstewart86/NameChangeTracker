from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class AppSettings(BaseSettings):
    SLACK_APP_TOKEN: str = "xoxb-12345-abcde"

    class Config:
        env_file = ".env"


app_settings = AppSettings()
