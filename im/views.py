from django.shortcuts import render_to_response

from VkaIM import common, buffers


# Create your views here.

def visit_im(request):
    user = get_user(request.GET.get('token'))
    friend_list = []
    if len(user.friends.all()) > 0:
        friend_list = common.ulist2arr(user.friends.all())
    return render_to_response('im/im_page.html', {'contact_list': friend_list})


def get_user(token):
    return buffers.buffer_user_list.get(token)
