from channels.handler import AsgiHandler
from django.http import HttpResponse


# def http_consumer(message):
#     response = HttpResponse("Vkazas! Your asked for %s" % message.content['path'])
#     for chunk in AsgiHandler.encode_response(response):
#         message.reply_channel.send(chunk)


def ws_message(message):
    message.reply_channel.send({
        "text": message.content['text'],
    })


def ws_connect(message):
    print(message)


def ws_disconnect(message):
    print(message)
