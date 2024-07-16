from kafka import KafkaProducer
from time import sleep

producer = KafkaProducer(bootstrap_servers='localhost:9092')

start_x = 100
start_y = 100
width = 800
height = 400
sleep(2)
for _ in range(5):
        # Print the coordinates
    for x in range(1, width+1,2):
        coordinates = f"{start_x+(x)}, {start_y}"
        print(coordinates)
        producer.send('chat', value=coordinates.encode('utf-8'))
    start_x = start_x + width
    for y in range(1, height+1,2):
        coordinates = f"{start_x}, {start_y+(y)}"
        print(coordinates)
        producer.send('chat', value=coordinates.encode('utf-8'))
    start_y = start_y + height
    for x in range(1, width+1, 2):
        coordinates = f"{start_x-(x)}, {start_y}"
        print(coordinates)
        producer.send('chat', value=coordinates.encode('utf-8'))
    start_x = start_x - width
    for y in range(1, height+1, 2):
        coordinates = f"{start_x}, {start_y-(y)}"
        print(coordinates)
        producer.send('chat', value=coordinates.encode('utf-8'))
    start_y = start_y - height