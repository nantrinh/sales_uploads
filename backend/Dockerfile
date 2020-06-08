# Choice of python base image:
# https://pythonspeed.com/articles/base-image-python-docker-images/
FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt  .
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && pip install -r requirements.txt
RUN mkdir api/
COPY api/* ./api/
COPY app.py run.sh ./ 
#ENTRYPOINT ["./app/run.sh"]