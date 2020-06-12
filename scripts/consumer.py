# -*- coding: utf-8 -*-

import json
from kafka import KafkaConsumer

# ==============================================================================
# GLOBAL
# ==============================================================================

brokers = ["localhost:9092"]
topico = "dados-tweets"
consumer = KafkaConsumer(topico, group_id = 'group1', bootstrap_servers = brokers)

frases = ""
for messagem in consumer:
  texto = json.loads(messagem.value.decode('utf-8'))
  print(texto)
  frases = frases + texto.get("text", "No Found")
  print(frases)
