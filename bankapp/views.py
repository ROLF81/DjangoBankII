from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from . models import Customers, Account
import json

def Home(request):
    return HttpResponse("welcome to your bank")

def getcustomers(request):
    if request.method == 'GET':
            customers = Customers.objects.all()
            if (not customers):
                return HttpResponseBadRequest ('there are no customers in the database')
            data = []
            print(customers)
            for i in customers:
                datalist = {'id':i.id, 'firstname':i.firstname, 'lastname':i.lastname, 
                             'password':i.password, 'isadmin':i.isadmin}
                data.append(datalist)
            datajson = json.dumps(data)
            print(datajson)
            resp = HttpResponse()
            resp.headers['content-type'] = 'text/json'
            resp.content = datajson
            return resp
    else:
        return HttpResponseNotAllowed(['GET'], 'metodo no permitido')

def getonecustomer(request, id_):
    if request.method == 'GET':
            customer = Customers.objects.filter(id = id_).first()
            if (not customer):
                return HttpResponseBadRequest ('Client does not exist')
            data = {'id':customer.id, 'firstname':customer.firstname, 'lastname':customer.lastname, 
                    'password':customer.password, 'isadmin':customer.isadmin}
            datajson2 = json.dumps(data)
            resp2 = HttpResponse()
            resp2.headers['content-type'] = 'text/json'
            resp2.content = datajson2
            return resp2
    else:
        return HttpResponseNotAllowed ('metodo invalido')


def newcustomer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            customer = Customers(
                id = data['id'],
                firstname = data ['firstname'],
                lastname = data['lastname'],
                email = data ['email'],
                password = data['password'],
                #isadmin = data['isadmin'],
            )

            customer.save()
            return HttpResponse('Customer successfully added')
        except:
            return HttpResponseBadRequest('error en los datos enviados')
    else:
        return HttpResponseNotAllowed(['POST'],'metodo invalido')

def updatecustomer(request, id_):
    if request.method == 'PUT':
        try:
            customer = Customers.objects.filter(id = id_).first()
            if (not customer):
                return HttpResponseBadRequest('client does not exist')

            data = json.loads(request.body)  
            customer.firstname = data ['firstname']
            customer.lastname = data['lastname']
            customer.email = data ['email']
            customer.password = data['password']
            
            customer.save()
            return HttpResponse('Customer successfully added')
        except:
            return HttpResponseBadRequest('error in the sent data')
    else:
        return HttpResponseNotAllowed(['PUT'],'invalid method')

def deletecustomer(request, id_):
    if request.method == 'DELETE':
        try:
            customer = Customers.objects.filter(id = id_).first()
            if (not customer):
                return HttpResponseBadRequest('client does not exist')
            
            customer.delete()
            return HttpResponse('Delete customer')
        except:
            return HttpResponseBadRequest('error in the sent data')
    else:
        return HttpResponseNotAllowed(['DELETE'],'invalid method')

#***************************************
#  Account
#***************************************

