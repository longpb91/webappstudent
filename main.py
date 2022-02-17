from src.app import app
import os
# from dotenv import load_dotenv


# load_dotenv()


if __name__ == "__main__":
    # app.secret_key = os.environ.get('SECRET_KEY')
    app.secret_key = os.getenv('SECRET_KEY')
    app.run(host='0.0.0.0', port='5000')

