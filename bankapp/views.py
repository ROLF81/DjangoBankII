from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from . models import Customers, Account
import json

def Home(request):
    return HttpResponse("welcome to your bank")

def getcustomers(request):
    if request.method == 'GET':
        try:
            customers = Customers.objects.all()
            data = []
            for i in customers:
                datalist = {'id':i.id, 'firstname':i.firstname, 'lastname':i.lastname, 
                             'password':i.password, 'isadmin':i.isadmin}
                data.append(datalist)
            datajson = json.dumps(datalist)
            resp = HttpResponse()
            resp.headers['content-type'] = 'text/json'
            resp.content = datajson
            return resp
        except:
            return HttpResponseBadRequest('error en los datos enviados')
    else:
        return HttpResponseNotAllowed(['GET'], 'metodo no permitido')

def getonecustomer(request, id_):
    if request.method == 'GET':
        try:
            customer = Customers.objects.filter(id = id_).first()
            data = {'id':customer.id, 'firstname':customer.firstname, 'lastname':customer.lastname, 
                    'password':customer.password, 'isadmin':customer.isadmin}
            datajson2 = json.dumps(data)
            resp2 = HttpResponse()
            resp2.headers['content-type'] = 'text/json'
            resp2.content = datajson2
            return resp2
        except:
            return HttpResponseBadRequest('error en los datos enviados')
    else:
        return HttpResponseNotAllowed ('metodo invalido')


