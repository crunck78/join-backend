from urllib import request
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

# Create your views here.

@csrf_exempt
def login(request):
    if request.method == 'GET':
        csrf_token = get_token(request)
        print(csrf_token)
        return HttpResponse("LOGIN WORKS")
    else:
       return HttpResponseBadRequest("BAD REQUEST")
   

@csrf_exempt
def register(request):
   
    if request.method == 'POST':
        csrf_token = get_token(request)
        print(csrf_token)
        return HttpResponse("REGISTER WORKS")
    else:
       return HttpResponseBadRequest("BAD REQUEST")
    