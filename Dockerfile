FROM daocloud.io/python:3.4
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir /code
WORKDIR /code
COPY . /code
COPY docker-entrypoint.sh docker-entrypoint.sh
RUN chmod +x docker-entrypoint.sh
EXPOSE 8000

ENTRYPOINT daphne VkaIM.asgi:channel_layer
CMD python manage.py runworker