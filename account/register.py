from django.db import IntegrityError

from account.models import User


def reg_to_database(user_info):
    if not check_info_valid(user_info):
        return -1

    try:
        User.objects.create(name=user_info.get('username'),
                            password=user_info.get('password'),
                            email=user_info.get('email'))
    except IntegrityError as e:  # duplicate username
        print(e)
        return -2
    except Exception as e:  # other errors
        print(e)
        return 0
    else:
        return 1


def check_info_valid(user_info):
    uname = user_info.get('username')
    password = user_info.get('password')
    email = user_info.get('email')

    if not (uname is None) and not (password is None) and not (email is None):
        return True
    else:
        return False

