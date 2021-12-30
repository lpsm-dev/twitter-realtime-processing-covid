<p align="center">
  <img alt="python-kafka" src="https://miro.medium.com/max/1400/1*SevEMhvGvosd6am1u0Qqqg.png" width="250px" float="center"/>
</p>

<h1 align="center">Welcome to Twitter Realtime Processing Repository</h1>

<p align="center">
  <strong>Python Realtime Processing Tweets COVID-19 using Kafka + Elasticsearch + Kibana + Docker + Docker-Compose</strong>
</p>

<p align="center">
  <a href="https://github.com/lpmatos/twitter-realtime-processing-covid">
    <img alt="Open Source" src="https://badges.frapsoft.com/os/v1/open-source.svg?v=102">
  </a>

  <a href="https://github.com/lpmatos/twitter-realtime-processing-covid/graphs/contributors">
    <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/lpmatos/twitter-realtime-processing-covid">
  </a>

  <a href="https://github.com/lpmatos/twitter-realtime-processing-covid">
    <img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/lpmatos/twitter-realtime-processing-covid">
  </a>

  <a href="https://github.com/lpmatos/twitter-realtime-processing-covid">
    <img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/lpmatos/twitter-realtime-processing-covid">
  </a>

  <a href="https://github.com/lpmatos/twitter-realtime-processing-covid/stargazers">
    <img alt="GitHub Stars" src="https://img.shields.io/github/stars/lpmatos/twitter-realtime-processing-covid?style=social">
  </a>

  <a href="https://github.com/lpmatos/twitter-realtime-processing-covid/commits/master">
    <img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/lpmatos/twitter-realtime-processing-covid">
  </a>

  <a href="https://github.com/lpmatos/twitter-realtime-processing-covid">
    <img alt="Repository Size" src="https://img.shields.io/github/repo-size/lpmatos/twitter-realtime-processing-covid">
  </a>

  <a href="https://github.com/lpmatos/twitter-realtime-processing-covid/issues">
    <img alt="Repository Issues" src="https://img.shields.io/github/issues/lpmatos/twitter-realtime-processing-covid">
  </a>

  <a href="https://github.com/lpmatos/twitter-realtime-processing-covid/blob/master/LICENSE">
    <img alt="MIT License" src="https://img.shields.io/github/license/lpmatos/twitter-realtime-processing-covid">
  </a>
</p>

### Menu

<p align="left">
  <a href="#pre-requisites">Pre-Requisites</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#description">Description</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#how-to-contribute">How to contribute</a>
</p>

### By me a coffe

Pull requests are welcome. If you'd like to support the work and buy me a ☕, I greatly appreciate it!

<a href="https://www.buymeacoffee.com/EatdMck" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 100px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

### Getting Started

If you want use this repository you need to make a **git clone**:

```bash
git clone --depth 1 https://github.com/lpmatos/twitter-realtime-processing-covid.git -b master
```

This will give access on your **local machine**.

### Pre-Requisites

To this project you yeed:

* Python 3.8.
* Docker and Docker Compose.
* Kafka ecosystem.
* Elasticsearch.
* Kiabana

### Built with

- [Python](https://www.python.org/)
- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### How to use it?

#### Locale

1. Set the application environment variables.
2. Install python packages in requirements.txt.
3. Run docker-compose.yml to deploy all kafka and elastic ecosystem.
4. Profit.

#### Docker

1. Set all environment variables in dot-env files.
2. Creathe a docker network.
3. Run docker-compose.yml to deploy all kafka and elastic ecosystem.
4. Run docker-compose-tools.to run the application.
5. Profit.

This system is fully containerised. You will need [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/) to run it.

You simply need to create a Docker network called `kafka-network` to enable communication between the Kafka cluster and the apps:

```bash
$ docker network create kafka-network
```

All set!

## ➤ Description <a name = "description"></a>

### Sending Data to Elasticsearch

```bash
curl -X POST kafka-connect:8083/connectors -H "Content-Type: application/json" -d '{
	"name": "elasticsearch-sink-kafka",
	"config": {
		"connector.class": "io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
		"type.name": "kafka-connect",
		"key.converter.schemas.enable": "false",
		"tasks.max": "1",
		"topics": "dados-tweets",
		"value.converter.schemas.enable": "false",
		"key.ignore": "true",
		"connection.url": " http://elasticsearch:9200",
		"value.converter": "org.apache.kafka.connect.json.JsonConverter",
		"key.converter": "org.apache.kafka.connect.storage.StringConverter",
		"schema.ignore": "true"
	}
}'
```

### Environment variables

**Name**  |  **Description**
:---:  |  :---:
**TWITTER_CONSUMER_KEY**  |  Twitter Consumer Key
**TWITTER_CONSUMER_SECRET**  |  Twitter Consumer Secret
**TWITTER_ACCESS_TOKEN**  |  Twitter Access Token
**TWITTER_ACCESS_TOKEN_SECRET**  |  Twitter Access Token Secret
**LOG_PATH**  |  Just the Log Path
**LOG_FILE**  |  Just the Log File
**LOG_LEVEL**  |  Just the Log Level
**LOGGER_NAME**  |  Just the Logger name
**KAFKA_BROKER_URL**  |  Kafka Broker URL
**KAFKA_TOPIC**  |  Kafka Topic Name

### Environment file

We use decouple for strict separation of settings from code. It helps us with to store parameters in .env file and properly convert values to correct data type.

Copy the file .env-example to a .env file and replace the values inside of it.

## ➤ Usage <a name = "usage"></a>

Ways to run and use this project.

<details><summary>Docker</summary>
<p>

Steps to build the Docker Image.

#### Build

```bash
docker image build -t <IMAGE_NAME> -f <PATH_DOCKERFILE> <PATH_CONTEXT_DOCKERFILE>
docker image build -t <IMAGE_NAME> . (This context)
```

#### Run

Steps to run the Docker Container.

* **Linux** running:

```bash
docker container run -d -p <LOCAL_PORT:CONTAINER_PORT> <IMAGE_NAME> <COMMAND>
docker container run -it --rm --name <CONTAINER_NAME> -p <LOCAL_PORT:CONTAINER_PORT> <IMAGE_NAME> <COMMAND>
```

* **Windows** running:

```
winpty docker.exe container run -it --rm <IMAGE_NAME> <COMMAND>
```

For more information, access the [Docker](https://docs.docker.com/) documentation or [this](docs/docker.md).
</p>
</details>

<details><summary>Docker-Compose</summary>
<p>

Build and run a docker-compose.

```bash
docker-compose up --build
```

Down all services deployed by docker-compose.

```bash
docker-compose down
```

Down all services and delete all images.

```bash
docker-compose down --rmi all
```
</p>
</details>

## ➤ Visuals <a name = "visuals"></a>

Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## ➤ Author <a name = "author"></a>

👤 **Lucca Pessoa**

Hey!! If you like this project or if you find some bugs feel free to contact me in my channels:

>
> * Email: lpsm-dev@protonmail.com
> * Website: https://github.com/lpmatos
> * GitHub: [@lpmatos](https://github.com/lpmatos)
> * GitLab: [@lpmatos](https://gitlab.com/lpmatos)
>

## ➤ Versioning <a name = "versioning"></a>

To check the change history, please access the [**CHANGELOG.md**](CHANGELOG.md) file.

## ➤ Troubleshooting <a name = "troubleshooting"></a>

If you have any problems, please contact [me](https://github.com/lpmatos).

## ➤ Project status <a name = "project-status"></a>

This project is currently undergoing a reorganization 👾.

## ➤ Show your support <a name = "show-your-support"></a>

<div align="center">

Give me a ⭐️ if this project helped you!

<p>
  <img alt="gif-header" src="https://www.icegif.com/wp-content/uploads/baby-yoda-bye-bye-icegif.gif" width="350px" float="center"/>
</p>

Made with 💜 by [me](https://github.com/lpmatos) :wave: inspired on [readme-md-generator](https://github.com/kefranabg/readme-md-generator)

</div>
