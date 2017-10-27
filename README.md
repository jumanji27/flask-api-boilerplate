setup example: https://realpython.com/blog/python/flask-by-example-part-1-project-setup/

pip3 install -r requirements.txt

echo "source `which activate.sh`" >> ~/.bash_profile
source ~/.bash_profile

pg_ctl -D /usr/local/var/postgres start

python manage.py db upgrade

docker build -t flask-simple-api -f env/Dockerfile .

