import os
from dotenv import load_dotenv
from flask import Flask
from board import pages, posts, database

load_dotenv()

# app = Flask(__name__)
# @app.route("/")
# def home():
#     return "Hello, World!"

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    database.init_app(app)
    
    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Database: {app.config.get('DATABASE')}")
    return app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
