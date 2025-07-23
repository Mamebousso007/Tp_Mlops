from confluent_kafka import Producer
import time

conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)
topic = "my_first_topic"

def delivery_report(err, msg):
    if err:
        print(f"❌ Message delivery failed: {err}")
    else:
        print(f"✅ Message delivered to {msg.topic()} [{msg.partition()}]")

for i in range(10):
    message = f"Message numéro {i}"
    producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
    producer.poll(0)
    time.sleep(1)

producer.flush()
