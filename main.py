from src.api import app_api
import os
from dotenv import load_dotenv


load_dotenv()

if __name__ == "__main__":
    app_api.secret_key = os.environ.get('SECRET_KEY')
    app_api.run()


