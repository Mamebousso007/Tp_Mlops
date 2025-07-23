from confluent_kafka import Consumer, KafkaException

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mon-groupe-python',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
topic = "my_first_topic"
consumer.subscribe([topic])

try:
    print("📡 En attente de messages...")
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        print(f"📨 Reçu: {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    print("🛑 Arrêt par l'utilisateur")
finally:
    consumer.close()
