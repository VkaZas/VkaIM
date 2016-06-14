import uuid

from django.core.exceptions import ObjectDoesNotExist

from VkaIM import buffers
from account.models import User, OnlineUser


def login_to_database(user_info):
    username = user_info.get('username')
    if username is None:
        return -2

    password = user_info.get('password')
    user = User.objects.get(name=username)
    # todo: fix this to fetch info from buffer first

    if user:
        if user.password != password:
            return -1, ''  # wrong password
        else:
            # login success
            token = uuid.uuid1()
            cur_oluser = None
            try:
                cur_oluser = OnlineUser.objects.get(user_id=user.id)
            except ObjectDoesNotExist:
                cur_oluser = OnlineUser.objects.create(token=token, user=user)
                buffers.buffer_user_list[token] = cur_oluser.user
                return 1, token, cur_oluser.user.id

            if cur_oluser is not None:
                buffers.buffer_user_list[cur_oluser.token] = cur_oluser.user
                return 0, cur_oluser.token, cur_oluser.user.id

    else:
        return -2, ''  # user doesn't exist


def logout_from_database(token):
    o_user = OnlineUser.objects.get(token=token)
    if o_user:
        o_user.delete()
        buffers.buffer_user_list[token] = None
        return 1
    else:
        return -1

