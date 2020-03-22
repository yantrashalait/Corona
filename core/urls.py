from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'news', views.NewsViewSet, basename='news')
router.register(r'aapatkalin', views.AapatKalinSewaViewSet, basename="aapatkalin")


urlpatterns = []

urlpatterns += router.urls
