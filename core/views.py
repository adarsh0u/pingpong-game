from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from django.contrib import messages 
from pathlib import Path
import os
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import threading
from .utils import mainfunc ,  closeapp
#custom views

def index(request):
    #if request.method == "POST":
    #    if request.POST.get("first") == 'first':
    #        mainfunc()
    #    elif request.POST.get("second")=='second':
    #        #closeall()
    #        pass
    return render(request, 'main/index.html')

def scan(request):
    if request.method=="GET":
        mainfunc()
    return HttpResponse()
    
def stop(request):
    if request.method=="GET":
        closeapp()
    return HttpResponse()