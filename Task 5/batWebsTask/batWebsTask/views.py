from django.http import HttpResponse
from django.shortcuts import render

def resumePage(request):
    return render(request,"index.html")