ARG PYTHON_VERSION=3.8-alpine3.11

FROM python:${PYTHON_VERSION} as base

FROM base as install-env

COPY [ "requirements.txt", "."]

RUN pip install --upgrade pip && \
    pip install --user --no-warn-script-location -r ./requirements.txt

FROM base

LABEL maintainer="Lucca Pessoa da Silva Matos - luccapsm@gmail.com" \
        org.label-schema.version="1.1.0" \
        org.label-schema.release-data="12-06-2020" \
        org.label-schema.url="https://github.com/lpmatos" \
        org.label-schema.alpine="https://alpinelinux.org/" \
        org.label-schema.python="https://www.python.org/" \
        org.label-schema.name="Twitter realtime processing tweets Covid-19 using Kafka"

RUN set -ex && apk update

RUN apk add --update --no-cache \
      bash=5.0.11-r1 \
      netcat-openbsd=1.130-r1 \
      curl=7.67.0-r0

COPY --from=install-env [ "/root/.local", "/usr/local" ]

WORKDIR /usr/src/code

COPY [ "./code", "." ]

RUN find ./ -iname "*.py" -type f -exec chmod a+x {} \; -exec echo {} \;;
