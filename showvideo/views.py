from django.shortcuts import render
from django.http import HttpResponse
from .models import Video


# Create your views here.
def hello(request):
    return HttpResponse("<h1>hello world</h1>")


def world(request):
    response = {"name":"Bogdan", "d":34,"arr":[1,2,3,4,5]}
    response["content"] = Video.objects.all()
    return render(request, "index.html", response)
