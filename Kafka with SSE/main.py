from flask import Flask, render_template, request
from flask_sse import sse
import threading
from time import sleep
from random import randint

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/push', methods=['POST'])
# def publish_message():
#     json_data = dict(request.json)
#     message = json_data.get("message")
#     sse.publish({"message": message}, type='greeting')
#     return "Message sent!"

def consume_messages():
    with app.app_context():
        while True:
            print("Message Produced!!")
            sse.publish({"message":str( randint(1, 99999999))}, type='greeting')
            sleep(0.5)

if __name__ == '__main__':
    consumer_thread = threading.Thread(target=consume_messages)
    consumer_thread.start()
    app.run(debug=True)