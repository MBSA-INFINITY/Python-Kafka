from flask import Flask, render_template
from flask_sse import sse
from kafka import KafkaConsumer
import threading
from time import sleep

app = Flask(__name__)
app.secret_key = 'mbsakaflaskkafkaredisapp'
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

consumer = KafkaConsumer('chat', bootstrap_servers='localhost:9092')

def consume_messages():
    for message in consumer:
        message = message.value.decode('utf-8')
        with app.app_context():
            sse.publish({"message": message}, type='greeting')

# Start Kafka consumer thread
consumer_thread = threading.Thread(target=consume_messages)
consumer_thread.start()

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/mbsa")
def mbsa():
    sleep(3)
    start_x = 100
    start_y = 100
    width = 800
    height = 400
    for _ in range(5):
            # Print the coordinates
        for x in range(1, width+1):
            coordinates = f"{start_x+(x)}, {start_y}"
            print(coordinates)
            sse.publish({"message": coordinates}, type='greeting')
        start_x = start_x + width
        for y in range(1, height+1):
            coordinates = f"{start_x}, {start_y+(y)}"
            print(coordinates)
            sse.publish({"message": coordinates}, type='greeting')
        start_y = start_y + height
        for x in range(1, width+1):
            coordinates = f"{start_x-(x)}, {start_y}"
            print(coordinates)
            sse.publish({"message": coordinates}, type='greeting')

        start_x = start_x - width
        for y in range(1, height+1):
            coordinates = f"{start_x}, {start_y-(y)}"
            print(coordinates)
            sse.publish({"message": coordinates}, type='greeting')

        start_y = start_y - height
    return "Production Completed"
    


if __name__ == '__main__':
    app.run(debug=True)