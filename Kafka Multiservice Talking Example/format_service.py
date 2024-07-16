from kafka import KafkaConsumer, KafkaProducer
from time import sleep

producer = KafkaProducer(bootstrap_servers='localhost:9092')
consumer = KafkaConsumer('compress', bootstrap_servers='localhost:9092')

def formatting_video():
    sleep(4)

def consume_messages():
    for message in consumer:
        message = message.value.decode('utf-8')
        print("Formatting Video")
        formatting_video()
        producer.send('format', value=message.encode('utf-8'))



consume_messages()