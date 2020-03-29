from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import NewsSerializer, AapatKalinSewaSerializer, NumberSerializer
from .models import News, AapatKalinSewa, Numbers


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def list(self, request, *args, **kwargs):
        print('adsadasdsad')
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            "data": serializer.data
        })

    def get_object(self, *args, **kwargs):
        return get_object_or_404(News, id=self.kwargs.get('pk'))

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response({
            "data": serializer.data
        })

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "data": serializer.errors
            })

        self.perform_create(serializer)
        return Response({
            "data": serializer.data
        })


class AapatKalinSewaViewSet(viewsets.ModelViewSet):
    serializer_class = AapatKalinSewaSerializer
    queryset = AapatKalinSewa.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            "data": serializer.data
        })

    def get_object(self, *args, **kwargs):
        return get_object_or_404(AapatKalinSewa, id=self.kwargs.get('pk'))

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response({
            "data": serializer.data
        })

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "data": serializer.errors
            })

        self.perform_create(serializer)
        return Response({
            "data": serializer.data
        })


class NumbersViewSet(viewsets.ModelViewSet):
    serializer_class = NumberSerializer
    queryset = Numbers.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            "data": serializer.data
        })

    def get_object(self, *args, **kwargs):
        return get_object_or_404(Numbers, id=self.kwargs.get('pk'))

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response({
            "data": serializer.data
        })

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "data": serializer.errors
            })

        self.perform_create(serializer)
        return Response({
            "data": serializer.data
        })
