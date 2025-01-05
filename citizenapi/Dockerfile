FROM python:3.11.2-slim-buster 

WORKDIR /usr/src/citizenapi

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/citizenapi/requirements.txt
RUN pip install -r requirements.txt

COPY ./citizenapi/entrypoint.sh /usr/src/citizenapi/entrypoint.sh
RUN chmod +x /usr/src/citizenapi/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/citizenapi/entrypoint.sh"]