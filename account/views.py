# coding=utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse

from account import register, login
from response_struct import build_resp


def visit_register(request):
    return render_to_response('account/register.html')


def do_register(request):
    if request.is_ajax() and request.method == 'POST':
        data = request.POST
        res = register.reg_to_database(data)
        if res > 0:
            return JsonResponse(build_resp('Registration succeeded', {}, True))
        elif res == -1:
            return JsonResponse(build_resp('Invalid info', {}, False))
        elif res == -2:
            return JsonResponse(build_resp('Duplicated username', {}, False))
        else:
            return JsonResponse(build_resp('Unexpected error', {}, False))


def visit_login(request):
    return render_to_response('account/login.html')


def do_login(request):
    if request.is_ajax() and request.method == 'POST':
        data = request.POST
        res, token = login.login_to_database(data)
        if res > 0:
            return JsonResponse(build_resp('Login success', {'token': token}, True))
        elif res == -1:
            return JsonResponse(build_resp('Wrong password', {}, False))
        elif res == -2:
            return JsonResponse(build_resp('User does not exist', {}, False))
        else:
            return JsonResponse(build_resp('Unexpected error', {}, False))


# @require_websocket
# def echo_once(request):
#     message = request.websocket.wait()

