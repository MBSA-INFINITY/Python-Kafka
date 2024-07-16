from flask import Flask, render_template, request
from kafka import KafkaProducer, KafkaConsumer
from flask_sse import sse
import threading

app = Flask(__name__)
app.secret_key = 'mbsakaflaskkafkaredisapp'
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

# Initialize Kafka producer and consumer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
consumer = KafkaConsumer('chat', bootstrap_servers='localhost:9092')

# Store received messages
chat_messages = []

def consume_messages():
    for message in consumer:
        message = message.value.decode('utf-8')
        with app.app_context():
            sse.publish({"message": message}, type='greeting')

# Start Kafka consumer thread
consumer_thread = threading.Thread(target=consume_messages)
consumer_thread.start()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/push', methods=['POST'])
def publish_message():
    json_data = dict(request.json)
    message = json_data.get("message")
    producer.send('chat', value=message.encode('utf-8'))
    return "Message sent!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)