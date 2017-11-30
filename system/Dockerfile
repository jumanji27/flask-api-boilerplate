FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip

COPY . /flask-api-boilerplate
WORKDIR /flask-api-boilerplate

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
