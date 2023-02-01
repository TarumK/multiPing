from django.shortcuts import render
from django.http import HttpResponse
from .models import Server
import json


def index(request):
    servers = Server.objects.all()

    return render(request, "index.html", {'servers': servers})


def ping(request):
    if request.method == 'POST':
        hostList = json.loads(request.body)['hostList']
        print(hostList)
        # do something with hostList
        ...
        return HttpResponse(hostList)
    # return render(request, 'ping.html', {})
