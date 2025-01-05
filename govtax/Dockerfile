FROM python:3.11.2-slim-buster 

WORKDIR /usr/src/govtax

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/govtax/requirements.txt
RUN pip install -r requirements.txt

COPY ./govtax/entrypoint.sh /usr/src/govtax/entrypoint.sh
RUN chmod +x /usr/src/govtax/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/govtax/entrypoint.sh"]