import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello there</h1>'

app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)

