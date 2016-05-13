from account.models import User, OnlineUser
import uuid


def login_to_database(user_info):
    username = user_info['username']
    password = user_info['password']
    user = User.objects.get(name=username)
    if user:
        if user.password != password:
            return -1, ''  # wrong password
        else:
            # login success
            token = uuid.uuid1()
            OnlineUser.objects.create(user=user, token=token)
            return 1, token
    else:
        return -2, ''  # user doesn't exist


def logout_from_database(token):
    o_user = OnlineUser.objects.get(token=token)
    if o_user:
        o_user.delete()
        return 1
    else:
        return -1

