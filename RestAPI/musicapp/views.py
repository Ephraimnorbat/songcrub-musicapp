from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import artiste
from .serializers import artisteSerializers
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
# Create your views here.

def artisteList(request):

    if request.method == 'GET':
        artiste1 = artiste.objects.all()
        serializer = artisteSerializers(artiste1,many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = artisteSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            


    #def post(self):
    #  pass

