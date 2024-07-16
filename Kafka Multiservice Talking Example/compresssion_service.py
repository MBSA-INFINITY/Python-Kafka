from kafka import KafkaConsumer, KafkaProducer
from time import sleep

producer = KafkaProducer(bootstrap_servers='localhost:9092')
consumer = KafkaConsumer('upload', bootstrap_servers='localhost:9092')

def compressing_video():
    sleep(4)

def consume_messages():
    for message in consumer:
        message = message.value.decode('utf-8')
        print("Compressing Video")
        compressing_video()
        producer.send('compress', value=message.encode('utf-8'))



consume_messages()