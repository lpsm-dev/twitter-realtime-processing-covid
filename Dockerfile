FROM python:3.9.6-alpine3.13 as base

FROM base as install
WORKDIR /tmp
COPY [ "requirements.txt", "."]
RUN set -ex && pip install --no-cache-dir \
      --user --no-warn-script-location \
      -r ./requirements.txt

FROM base
RUN set -ex && apk update && \
    apk add --update --no-cache \
      bash=5.1.0-r0 \
      netcat-openbsd=1.130-r2 \
      curl=7.79.1-r0
COPY --from=install [ "/root/.local", "/usr/local" ]
WORKDIR /usr/src/code
COPY [ "./code", "." ]
RUN find ./ -iname "*.py" -type f -exec chmod a+x {} \; -exec echo {} \;;
