import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    origins = os.getenv("ORIGINS").split(",")
    secret_key = os.getenv("SECRET_KEY")


settings = Settings()