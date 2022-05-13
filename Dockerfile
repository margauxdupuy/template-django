FROM python:3.9-slim-bullseye

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/usr/local/lib/python3.9

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Update system and pip dependencies
COPY requirements /tmp/requirements
RUN /bin/sh -c '''apt-get update && \
                  apt-get -y upgrade && \
                  pip install --upgrade pip && \
                  pip install pip-tools && \
                  pip install -r /tmp/requirements/dev.txt && \
                  apt-get autoremove -y && apt-get autoclean -y'''

WORKDIR /opt/template-django
COPY ./app /opt/template-django/app
COPY ./template-django /opt/template-django/template-django
COPY ./manage.py /opt/template-django/manage.py
