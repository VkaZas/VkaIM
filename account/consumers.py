import json

from channels.handler import AsgiHandler
from django.http import HttpResponse

from VkaIM import buffers
from im.message import convey_message, query_user_message

import time


def http_consumer(message):
    response = HttpResponse("Vkazas! Your asked for %s" % message.content['path'])
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)


def http_consumer2(message):
    response = HttpResponse("Vkazas! Your asked for %s" % message.content['path'])
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)


def ws_message(message):
    msg_dic = json.loads(message.content['text'])  # msg_dic = { message, target, uid}
    if msg_dic.get('query') == "1":
        query_user_message(msg_dic.get('uid'), msg_dic.get('target'), message.reply_channel)
    else:
        msg_dic['send_time'] = time.time()
        convey_message(msg_dic)


def ws_connect(message):
    uid = message.content.get('query_string')
    uid = uid[4:]
    buffers.buffer_user_reply[uid] = message.reply_channel


def ws_disconnect(message):
    print(message)


