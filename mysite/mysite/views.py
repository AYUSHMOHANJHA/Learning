#this file is created by me 

from django.http import HttpResponse

def index(request):
    return HttpResponse("hello ayush")


def about(request):
    return HttpResponse("<i>about hello ayush</i>")