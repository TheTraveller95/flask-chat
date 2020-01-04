import os
from flask import Flask, redirect, render_template, request, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []

def add_messages(username, message):
    """Add messages to the 'messages' list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timestamp":now , "from": username , "message": message}
    messages.append(messages_dict)

#def get_all_messages():
#    """Get all messages and searate them with a 'br'"""
#    return '<br>'.join(messages)

@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"]=request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template('index.html')

@app.route('/<username>') #this will return Hi username every time we put a username inside the url preceded by /
def user(username):
    """Display chat messages"""
    return render_template ('chat.html', username = username , chat_messages = messages)

@app.route('/<username>/<message>') #this will return username: message every time we put a username inside the url preceded by / and then /+message
def send_message(username, message):
    """Create a message and  redirect cack to the chat page"""
    add_messages(username, message)
    return redirect('/' + username)



app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)

