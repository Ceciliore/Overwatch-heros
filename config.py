from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Config:
    api_root = "/v1/overwatch"

    user = getenv("OVERWATCH_DB_USER")
    password = getenv("OVERWATCH_DB_PASSWORD")
    host = getenv("OVERWATCH_DB_HOST", "127.0.0.1")
    port = getenv("OVERWATCH_DB_PORT", "5432")
    database= getenv("OVERWATCH_DB_NAME")
