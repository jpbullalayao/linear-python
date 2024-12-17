import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    API_KEY = os.getenv("LINEAR_API_KEY")
    DEFAULT_TEAM_ID = os.getenv("LINEAR_TEAM_ID")
