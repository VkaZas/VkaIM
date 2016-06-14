def user2dict(user):
    res = {
        'id': user.id,
        'name': user.name,
    }
    return res


def ulist2arr(ulist):
    res = []
    for user in ulist:
        res.append(user2dict(user))
    return res


def msg2dict(msg):
    res = {
        'uid': msg.send_user,
        'target': msg.receive_user,
        'send_time': msg.send_time.strftime('%Y-%m-%d %H-%M-%S'),
        'message': msg.text,
        'receive_flag': msg.receive_flag
    }
    return res


def msglist2arr(msglist):
    res = []
    for msg in msglist:
        res.append(msg2dict(msg))
    return res
