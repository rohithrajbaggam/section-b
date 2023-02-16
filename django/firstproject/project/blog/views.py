from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import views, generics
from rest_framework.response import Response
from .models import BlogDataModel
from .serializers import BlogDataModelSerializer
# Create your views here.


class BlogDataGenericListAPIView(generics.ListCreateAPIView):
    queryset = BlogDataModel.objects.all()
    serializer_class = BlogDataModelSerializer














class BlogDataGenericAPIView(generics.GenericAPIView):
    queryset = BlogDataModel.objects.all()
    serializer_class = BlogDataModelSerializer

    def get(self, request):
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Data is Inserted"})
        else:
            return Response({
                "message" : f"Something went wrong, {serializer.errors}"})


class BlogDataUpdateDeleteGenericAPIView(generics.GenericAPIView):
    queryset = BlogDataModel.objects.all()
    serializer_class = BlogDataModelSerializer

    def get(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except: 
            return Response({'message' : "Data not found"})

    def put(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(instance=queryset ,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Data is Inserted"})
            else:
                return Response({
                    "message" : f"Something went wrong, {serializer.errors}"})
        except: 
            return Response({'message' : "Data not found"})
            
    def delete(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            queryset.delete()
            return Response({"message" : "Data Deleted"})
        except: 
            return Response({'message' : "Data not found"})
        



class BlogDataAPIView(views.APIView):

    def get(self, request):
        queryset = BlogDataModel.objects.all()
        # print(queryset)
        serializer = BlogDataModelSerializer(queryset, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = BlogDataModelSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Data Inserted"})
        else:
            return Response({
                "message" : f"Something went wrong, {serializer.errors}"})


class DummyAPI(views.APIView):
    def get(self, request):
        data = {
            "name" : "max",
            "title" : "First Post",
            "description" : "Dummy description"
        }
        return Response(data)


def dummyAPI(request):
    data = {
        "name" : "max",
        "title" : "First Post",
        "description" : "Dummy description"
    }
    return JsonResponse(data)



