# Songs

## How to run
* Set up postgresql db
* Replace all files that end with .dist with your own
    **Fill out your own data**
    - .env.dist -> .env
    - .my_pgpass.dist -> .my_pgpass
    - .pg_serivce.conf.dist -> .pg_service_conf
* Run next commands:
```
source scripts/setup.sh
pip install requirements.txt
python manage.py runserver
```

## Testing
```
python manage.py test
```
Runs all tests

