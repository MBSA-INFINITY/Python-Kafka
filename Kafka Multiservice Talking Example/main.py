from flask import Flask, render_template, session
from kafka import KafkaConsumer, KafkaProducer
from flask_sse import sse
from time import sleep
from random import randint
import threading


app = Flask(__name__)
app.secret_key = 'mbsakaflaskkafkaredisapp'
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

producer = KafkaProducer(bootstrap_servers='localhost:9092')
compress_consumer = KafkaConsumer('compress', bootstrap_servers='localhost:9092', group_id='my_favorite_group')
format_consumer = KafkaConsumer('format', bootstrap_servers='localhost:9092', group_id='my_favorite_group',)


def consume_compress_messages():
    for message in compress_consumer:
        message = message.value.decode('utf-8')
        print(message)
        num = message
        with app.app_context():
            print("consume sse called")
            message = f"Video Compressed Successfully! {message}"
            sse.publish({"message": message}, type=num)

# Start Kafka consumer thread
compress_consumer_thread = threading.Thread(target=consume_compress_messages)
compress_consumer_thread.start()

def format_compress_messages():
    for message in format_consumer:
        message = message.value.decode('utf-8')
        num = message
        with app.app_context():
            print("format sse called")
            message = f"Video Formatted Successfully! {message}"
            sse.publish({"message": message}, type=num)

# Start Kafka consumer thread
format_consumer_thread = threading.Thread(target= format_compress_messages)
format_consumer_thread.start()

@app.route("/")
def start():
    num = randint(1,9999999)
    session['num'] = str(num)
    return render_template("index.html", num=num)

@app.route("/upload")
def upload():
    num = session.get("num")
    sse.publish({"message": f"Video Upload Started - {num}"}, type=session.get('num'))
    sleep(2)
    sse.publish({"message": f"Video Uploaded Successfully!! - {num}"}, type=session.get('num'))
    message = str(num)
    producer.send('upload', value=message.encode('utf-8'))
    return "sent"

if __name__ == '__main__':
    app.run(debug=True)