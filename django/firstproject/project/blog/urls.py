from .views import DummyAPI, BlogDataAPIView, BlogDataGenericAPIView, BlogDataUpdateDeleteGenericAPIView, BlogDataGenericListAPIView
from django.urls import path 

urlpatterns = [
    path("dummy-api/", DummyAPI.as_view(), name="DummyAPI"),
    path("blog-list/<id>/", BlogDataUpdateDeleteGenericAPIView.as_view(), name="BlogDataUpdateDeleteGenericAPIView"),
    path("blog-list/", BlogDataGenericAPIView.as_view(), name="BlogDataGenericAPIView"),
    path("blog-list-api-view/", BlogDataGenericListAPIView.as_view(), name="BlogDataGenericListAPIView")   ,
]

