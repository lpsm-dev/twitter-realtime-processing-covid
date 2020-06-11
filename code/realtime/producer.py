from datetime import datetime
import tweepy
from json import dumps
from kafka import KafkaProducer

consumer_key = "2RbAEUM6BGKKeghcZohUV2N6m"
consumer_secret = "8szJ6lV9U9m0CVvoNKEZD1Yc9DrxncDNcVYClMqlzV5uOsYrz3"
access_token = "1224694128992112641-UDdWYhikO1MQiEY6x8TuwzspILBA8V"
access_token_secret = "zOmWcaMFpwDK1kxEAn8LEs0LPf6pPfY1mRDQoiEUszxqA"

broker = "localhost:9092"
topico = "dados-tweets"
producer = KafkaProducer(bootstrap_servers=[broker],
  value_serializer=lambda x: dumps(x).encode("utf-8")
)
                         
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweets = api.search("covid")

for tweet in tweets:
  frase = str(tweet.text)
  print(frase)
  data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  dados = {
    "tweet": frase, 
    "horario": data
  }
  producer.send(topico, value=dados)
