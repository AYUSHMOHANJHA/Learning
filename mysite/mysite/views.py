#this file is created by me 

from django.http import HttpResponse

def index(request):
    return HttpResponse("hello ayush")


def about(request):
    return HttpResponse("<i>about hello ayush</i>")

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("new liner remove")

def spaceremove(request):
    return HttpResponse("space remove <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("charcount")