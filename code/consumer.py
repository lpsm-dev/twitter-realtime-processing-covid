from kafka import KafkaConsumer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json
from IPython.display import clear_output

brokers = ["localhost:9092"]
topic = "dados-tweets"
consumer = KafkaConsumer(topic, group_id="group1", bootstrap_servers = brokers)

print(consumer)

frases = ""
print("Loop consumer")
for messagem in consumer:
    print(messagem)
    texto = json.loads(messagem.value.decode('utf-8'))
    frases = frases + texto['tweet']
    print(frases)
    clear_output()
    wordcloud = WordCloud(max_font_size=100, width = 1520, height = 535).generate(frases)
    plt.figure(figsize=(16,9))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    