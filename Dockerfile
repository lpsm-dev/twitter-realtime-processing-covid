FROM python:3.9.6-alpine3.13 as base

FROM base as install-env
COPY [ "requirements.txt", "."]
RUN pip install --upgrade pip && \
    pip install --user --no-warn-script-location -r ./requirements.txt

FROM base
RUN set -ex && apk update && \
    apk add --update --no-cache \
      bash=5.0.11-r1 \
      netcat-openbsd=1.130-r1 \
      curl=7.67.0-r0
COPY --from=install-env [ "/root/.local", "/usr/local" ]
WORKDIR /usr/src/code
COPY [ "./code", "." ]
RUN find ./ -iname "*.py" -type f -exec chmod a+x {} \; -exec echo {} \;;
