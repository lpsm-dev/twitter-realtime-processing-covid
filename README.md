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

### Sending Data to Elasticsearch

```
{
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
}
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

### Environment file

We use decouple for strict separation of settings from code. It helps us with to store parameters in .env file and properly convert values to correct data type.

Copy the file .env-example to a .env file and replace the values inside of it.

### 🐋 Development with Docker

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

### 🐋 Development with Docker Compose

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

### How to contribute

>
> 1. Make a **Fork**.
> 2. Follow the project organization.
> 3. Add the file to the appropriate level folder - If the folder does not exist, create according to the standard.
> 4. Make the **Commit**.
> 5. Open a **Pull Request**.
> 6. Wait for your pull request to be accepted.. 🚀
>
Remember: There is no bad code, there are different views/versions of solving the same problem. 😊

### Add to git and push

You must send the project to your GitHub after the modifications

```bash
git add -f .
git commit -m "Added - Fixing somethings"
git push origin master
```

### Versioning

- [CHANGELOG](CHANGELOG.md)

### License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

### Author

👤 **Lucca Pessoa**

Hey!! If you like this project or if you find some bugs feel free to contact me in my channels:

> * Email: luccapsm@gmail.com
> * Website: https://github.com/lpmatos
> * Github: [@lpmatos](https://github.com/lpmatos)
> * LinkedIn: [@luccapessoa](https://www.linkedin.com/in/lucca-pessoa-4abb71138/)

### Show your support

Give a ⭐️ if this project helped you!

### Project Status

* ✔️ Finish

---

<p align="center">Feito com ❤️ by <strong>Lucca Pessoa :wave:</p>
