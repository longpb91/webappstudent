from src.api import app
import os
# from dotenv import load_dotenv
#
#
# load_dotenv()

if __name__ == "__main__":
    app.secret_key = os.environ.get('SECRET_KEY')
    app.run()





