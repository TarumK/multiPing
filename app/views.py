from time import sleep

import ping3
from django.shortcuts import render
from django.http import HttpResponse
from .models import Server, Log
from ping3 import ping, verbose_ping
import json


def index(request):
    servers = Server.objects.all()

    return render(request, "index.html", {'servers': servers})


def go_ping(request):
    if request.method == 'POST':
        hostList = json.loads(request.body)['hostList']
# количество оправляемых пакетов
        count = 10
        for host in hostList:
            print(host)
            for i in range(1, count+1):
                time_response = ping(host, size=128, unit='s')
                if time_response is not False:
                    print(host, str(i) + ':' + "%.10f" % time_response)
                    sleep(0.1)
                else:
                    print(f'Хост {host} не отвечает...')
# среднее время отклика
            average = time_response/count

# записываем результаты в таблицу Log
            log = Log()
            log.host = host
            log.packet_count = count
            log.average_time = average
            log.save()

        return HttpResponse(hostList)
    # return render(request, 'ping.html', {})


def hostping(host_ip):
    average = 0.00000
    ip = f'{host_ip}'
    time_response = 0.000000
    ping_count = 10         #Количество отправляемых пакетов
    lost_count = 0          #Количество потерянных пакетов
    size_package = 128       #Размер отправляемых пакетов в байтах
    for count in range(1, ping_count + 1):
        time_response = ping(ip, size=size_package, unit='s')
        if time_response is not False:
            # print(f'{count}: Ответ от {ip}: время = {"%.6f" % (time_response)}')
            average = average + time_response
            # print('█' , end='')
            # time.sleep(0.05)
        else:
            # print(f'Хост {ip} не отвечает')
            lost_count += 1
    # print('**************************************')
    # print(' ► Хост:', host_ip)
    # print(f'Среднее время отклика для {ip} = {"%.6f" % (average/ping_count)}')
    # print(f'Отправлено пакетов: {ping_count}')
    # print(f'Потеряно пакетов: {lost_count}')
    # print(f'Процент потерь пакетов: {int(lost_count/ping_count*100)}%')
    sr = average/ping_count
    return [ping_count, sr]
