from kafka import KafkaConsumer
brokers = ["localhost:9092"]
topic = "dados-tweets"
consumer = KafkaConsumer(topic, group_id="group1", bootstrap_servers = brokers)

print(consumer)

frases = ""
print("Loop consumer")
for messagem in consumer:
    print(messagem)
