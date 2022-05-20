from ast import Constant
from django.shortcuts import render
from rest_framework import generics, views, status
from .serializer import *
from rest_framework.response import Response
from .models import *
from django.core import serializers


# Create your views here.

# for rest framework
class UrlList(generics.ListAPIView):
    queryset = Url.objects.all()
    serializer_class = OnlyUrlSerializer

class AuthList(generics.ListAPIView):
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer

class StatusList(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

# for API       
class UrlPost(views.APIView):
    def post(self, request):
        """ {urls: [....]} """
        urls = [Url(url=url) for url in request.data["urls"] if not Url.objects.filter(url=url).exists()]
        if len(urls) == 0:
            return Response({"status": "success"}, status=status.HTTP_200_OK)

        Url.objects.bulk_create(
            urls, len(urls))
        return Response({"status": "success"}, status=status.HTTP_200_OK)

    def delete(self, request):
        Url.objects.all().delete()
        return Response({"status": "success"}, status=status.HTTP_200_OK)


class AuthPost(views.APIView):
    def post(self, request):
        Auth(**request.data).save()
        return Response({"status": "success"}, status=status.HTTP_200_OK)
  
    def delete(self, request):
        Auth.objects.all().delete()
        return Response({"status": "success"}, status=status.HTTP_200_OK)

# for rest framework
class AuthDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer

class UrlDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

import json
def serialize_auth(start, end):
    return Auth.objects.all()[start: end].values("auth_provider_x509_cert_url", "auth_uri", "client_email", "client_id", "client_x509_cert_url", "id", "private_key", "private_key_id", "project_id", "status", "token_uri", "type")

def serialize_url(start, end):  
    return Url.objects.all()[start: end].values_list("url", flat=True)
   
class GetData(generics.ListAPIView):
    def get(self, request):
        start = request.data["start"]
        end = request.data["end"]
        return Response({
           "auth": serialize_auth( start, end),
            "url": serialize_url(start, end),
        }, status=status.HTTP_200_OK)

    def post(self, request):
        """ returns count of data in db"""
        return Response({
            "json": Auth.objects.count(),
            "url": Url.objects.count(),
            "processed": Status.objects.count(),
            "success": Status.objects.filter(status=200).count()
        },  status=status.HTTP_200_OK)

    def delete(self, request):
        Status.all().delete()