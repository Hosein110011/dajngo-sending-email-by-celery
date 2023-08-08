from django.shortcuts import render
from django.http import HttpResponse
from app.tasks import send_mail_func


def index(request):
    return HttpResponse('Don!')


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse('sent')