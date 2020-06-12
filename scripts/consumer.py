# importando as bibliotecas
from kafka import KafkaConsumer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json
from IPython.display import clear_output

brokers = ["localhost:9092"]
topico = "dados-tweets"
consumer = KafkaConsumer(topico, group_id = 'group1', bootstrap_servers = brokers)

frases = ""
for messagem in consumer:
  texto = json.loads(messagem.value.decode('utf-8'))
  print(texto)
  frases = frases + texto.get("text", "No Found")
  print(frases)
  clear_output()
  wordcloud = WordCloud(max_font_size=100, width = 1520, height = 535).generate(frases)
  plt.figure(figsize=(16,9))
  plt.imshow(wordcloud)
  plt.axis("off")
  plt.show()
