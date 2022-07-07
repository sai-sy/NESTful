FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache

WORKDIR /nespl-db-restful

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]