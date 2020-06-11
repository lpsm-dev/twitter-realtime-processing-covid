# Docker Commands

This is a list with some Docker commands. I hope that help you! 😊

## Exec

Enter inside a container.

```bash
docker exec -it <CONTAINER_NAME> <COMMAND>
```

## Cleaning

Clean your Docker environment.

```bash
docker system prune -af
```

*  Stop all containers.

```bash
docker stop $(docker ps -aq)
```

*  Remove all containers.

```bash
docker rm $(docker ps -aq)
```

*  Remove all images.

```bash
docker rmi $(docker images -a)
```

*  Remove all volumes.

```bash
docker volume prune -f
```

*  Remove all network.

```bash
docker network prune -f
```
