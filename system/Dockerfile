FROM ubuntu:17.10

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip

RUN rm -rf env
COPY . /flask-api-boilerplate
WORKDIR /flask-api-boilerplate

RUN pip3 install -r requirements.txt

RUN virtualenv env
RUN /bin/bash -c "source env/bin/activate"
ENV APP_SETTINGS="config.ProductionConfig"

CMD ["gunicorn", "app:app", "--log-level", "debug"]
