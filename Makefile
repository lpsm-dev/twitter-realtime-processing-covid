.PHONY: clean python-packages install run all

# ==============================================================================
# DECLARING VARIABLES
# ==============================================================================

# CONTAINERS
DOCKER_CONTAINER_LIST:=$(shell docker ps -aq)

# ==============================================================================
# DOCKER
# ==============================================================================

system:
	docker system prune -af

volume:
	docker volume prune -f

network:
	docker network prune -f

stop:
	docker stop ${DOCKER_CONTAINER_LIST}

remove:
	docker rm ${DOCKER_CONTAINER_LIST}

# ==============================================================================
# DOCKER-COMPOSE
# ==============================================================================

compose:
	docker-compose up --build

back:
	docker-compose up --build -d

down:
	docker-compose down

# ==============================================================================
# PYTHON
# ==============================================================================

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete
	find . -type d -name __pycache__ -delete

python-packages:
	pip3 install -r requirements.txt

install: python-packages

run:
	python3 code/main.py

all: clean install run
