from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room
import threading
import requests
from time import sleep

socketio = SocketIO()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

socketio.init_app(app)

room_no = 123

@app.route("/")
def start():
    return "Flask server is running!!"

@app.route("/chat")
def chat():
    return render_template("index.html")

@app.route('/producer')
def producer_data():
    consume_messages()
    # socketio.emit('mbsa', {'msg': "sai aditya"})
    return "message sent"

@socketio.on('joined')
def joined(message):
    # join_room(room_no)
    print("Room Joined!!")
    for i in range(5):
        socketio.emit('message', {'msg': "mbsa"+ ' has entered the room.'})


def consume_messages():
    while True:
        print("Message Produced!!")
        socketio.emit('mbsa', {'msg': "sai aditya"})
        sleep(2)

if __name__ == '__main__':
        # Start Kafka consumer thread
    # consumer_thread = threading.Thread(target=consume_messages)
    # consumer_thread.start()
    socketio.run(app)
