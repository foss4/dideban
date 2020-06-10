FROM python:3.8

WORKDIR /code

COPY requirements/base.txt /code/
COPY requirements/production.txt /code/
RUN pip install -r production.txt
COPY . /code/

EXPOSE 8000

CMD ["bash", "docker-entrypoint.sh"]