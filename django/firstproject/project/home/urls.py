from .views import homeView, aboutView, helpView, helloNameView
from django.urls import path 

urlpatterns = [

    path("hello/<name>/", helloNameView, name="helloNameView"),

    path("home/", homeView, name="homeView"),
    path("about/", aboutView, name="aboutView"),
    path("help/", helpView, name="helpView")
]
