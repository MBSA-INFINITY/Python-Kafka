from kafka import KafkaProducer, KafkaConsumer
from time import sleep
import threading

consumer = KafkaConsumer('mbsaiaditya', bootstrap_servers='localhost:9092')

# Store received messages
chat_messages = []

def function(message):
    print(message)
    sleep(2)
    print("Thread Complete")

def consume_messages():
    for message in consumer:
        message = message.value.decode('utf-8')
        new_thread = threading.Thread(target=function, args=(message,))
        new_thread.start()
        # function(message)

consume_messages()
