from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def helloNameView(request, name):
    # return HttpResponse(f"Hello, {name}")
    data = {
        "name" : name 
    }
    return render(request, "hello.html", context=data)





def homeView(request):
    # return HttpResponse("Home Page!")
    return render(request, "home.html")

def aboutView(request):
    # return HttpResponse("About Page!")
    return render(request, "about.html")

def helpView(request):
    # return HttpResponse("Help Page!")
    return render(request, "help.html")
