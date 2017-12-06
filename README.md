setup example: https://realpython.com/blog/python/flask-by-example-part-1-project-setup/

### Local

    echo "source `which activate.sh`" >> ~/.bash_profile
    source ~/.bash_profile

    pip3 install -r requirements.txt

    python manage.py db init/migrate/upgrade


    pg_ctl -D /usr/local/var/postgres start

### Docker

    docker build -t flask-api-boilerplate:latest -f system/Dockerfile .
    docker run -d -p 5000:5000 flask-api-boilerplate

### Compose

    docker-compose -f system/docker-compose.yml up

### Docker/Compose Migrations

docker exec -it dockerflask_flaskapp_1 bash -c "python manage.py db init/migrate/upgrade"