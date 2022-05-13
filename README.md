# template-django


## Developement

### Run server locally
```
docker compose up [web]
```

### Run commands inside the web container
```
docker-compose run --rm web bash
```

### Stop and/or remove local containers
```
docker compose stop  # Stops containers without removal. Content of local DB will be kept.
docker compose down  # Stops and remove containers. Content of local DB will be lost
```

### Install dependencies

- requirements/base.txt is common to all environments
- requirements/dev.txt is for dev environment

 ```
add your library in requirements/dev.in
docker compose run web pip-compile -r requirements/dev.in # dev.txt is automatically generated
docker compose run web pip install -r requirements/dev.txt
docker-compose build
```


## Endpoints
