from VkaIM import buffers, common
from im.models import Message
from django.db.models import Q
import json


def convey_message(msg_dic):
    tid = msg_dic.get('target')
    reply_channel = buffers.buffer_user_reply.get(str(tid))
    if reply_channel is not None:
        reply_channel.send({
            'text': json.dumps(msg_dic)
        })
    Message.objects.create(text=msg_dic.get('message'),
                           send_user=msg_dic.get('uid'),
                           receive_user=msg_dic.get('target'),
                           receive_flag=(reply_channel is not None))


def query_user_message(uid, target, reply_channel):
    msg_qset = Message.objects.filter((Q(send_user=uid) & Q(receive_user=target)) |
                                      (Q(send_user=target) & Q(receive_user=uid))).order_by("send_time")
    msg_list = common.msglist2arr(msg_qset)
    reply_channel.send({
        'text': json.dumps({'data': msg_list, 'buffer': "1", 'bf_uid': target})
    })

