ifeq ($(OS), Windows_NT)
	DOCKER_CONTAINER_LIST = $(shell docker ps -aq)
else
	DOCKER_CONTAINER_LIST = $(shell docker ps -aq)
endif

.PHONY: dsp
dsp:
	@-docker system prune -af

.PHONY: dvp
dvp:
	@-docker volume prune -f

.PHONY: dnp
dnp:
	@-docker network prune -f

.PHONY: ds
ds:
	$(if $(strip $(DOCKER_CONTAINER_LIST)), docker stop $(DOCKER_CONTAINER_LIST))

.PHONY: dv
dv:
	$(if $(strip $(DOCKER_CONTAINER_LIST)), docker rm $(DOCKER_CONTAINER_LIST))

.PHONY: create-network
create-network:
  docker network create network-default
  docker network create network-realtime-processing

.PHONY: clean
clean: ds dr dvp dnp

.PHONY: remove
remove: ds dr dvp dnp dsp

# ==============================================================================
# DOCKER-COMPOSE
# ==============================================================================

.PHONY: dcbn
dcbn:
	docker-compose build --no-cache

.PHONY: dcub
dcub:
	docker-compose up --build

.PHONY: dcubd
dcubd:
	docker-compose up --build -d

.PHONY: dcs
dcs:
	docker-compose down

.PHONY: dcps
dcps:
	docker-compose ps

.PHONY: run
run: dcps dcs dcubd
