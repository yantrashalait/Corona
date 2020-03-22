from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import NewsSerializer, AapatKalinSewaSerializer
from .models import News, AapatKalinSewa


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class AapatKalinSewaViewSet(viewsets.ModelViewSet):
    serializer_class = AapatKalinSewa
    queryset = AapatKalinSewa.objects.all()
