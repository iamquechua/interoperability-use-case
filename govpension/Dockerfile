FROM python:3.11.2-slim-buster 

WORKDIR /usr/src/govpension

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/govpension/requirements.txt
RUN pip install -r requirements.txt

COPY ./govpension/entrypoint.sh /usr/src/govpension/entrypoint.sh
RUN chmod +x /usr/src/govpension/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/govpension/entrypoint.sh"]