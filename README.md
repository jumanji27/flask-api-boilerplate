setup example: https://realpython.com/blog/python/flask-by-example-part-1-project-setup/


echo "source `which activate.sh`" >> ~/.bash_profile
source ~/.bash_profile

pip3 install -r requirements.txt

python manage.py db upgrade


pg_ctl -D /usr/local/var/postgres start


docker build -t flask-api-boilerplate:latest -f system/Dockerfile .
docker run -d -p 5000:5000 flask-api-boilerplate