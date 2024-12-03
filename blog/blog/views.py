from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')
   # return HttpResponse("Головна сторінка")

def contactpage(request):
    return render(request, 'contact.html')
    #return HttpResponse("Контакти")

def newspage(request):
    return render(request, 'news.html')

