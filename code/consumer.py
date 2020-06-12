# importando as bibliotecas
import json
from kafka import KafkaConsumer

brokers = ["kafka:9092"]
topico = "dados-tweets"
consumer = KafkaConsumer(topico, group_id = 'group1', bootstrap_servers = brokers)

if consumer.bootstrap_connected():
  print("Connection okay.")
  frases = ""
  for messagem in consumer:
    texto = json.loads(messagem.value.decode('utf-8'))
    print(texto)
    frases = frases + texto.get("text", "No Found")
    print(frases)
else:
  print("Bad")
