import os
from flask import Flask, redirect, render_template, request, session, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.getenv("SECRET" , "randomstring123")
messages = []

def add_message(username, message):
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
        return redirect(url_for("user", username = session["username"]))

    return render_template('index.html')

@app.route('/chat/<username>', methods=["GET","POST"]) 
def user(username):
    """Display chat messages"""
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username = session["username"])) # here we use the redirect instead of render_ttemplate because otherwise the message we wrote will be added every 5 sec in an infinite loop

    return render_template ('chat.html', username = username , chat_messages = messages)

'''@app.route('/<username>/<message>') #this will return username: message every time we put a username inside the url preceded by / and then /+message
def send_message(username, message):
    """Create a message and  redirect cack to the chat page"""
    add_message(username, message)
    return redirect('/' + username)'''


#app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True) #we use this during the project development
app.run(host=os.getenv('IP', "0.0.0.0"), port=os.getenv('PORT', "5000"), debug=False) # we use this when the project is completed and ready to be deployed

