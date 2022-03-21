from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv('.env')
word=os.getenv('WORD')
app = Flask(__name__)
@app.route('/')
def index():
    display="Hello,World!! "+word
    return display 
app.run(host='0.0.0.0', port=82)
