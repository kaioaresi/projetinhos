FROM python:3.5

WORKDIR /usr/src/app

COPY docker_remote.py ./

RUN pip install --no-cache-dir docker

CMD ["python3","docker_remote.py"]
