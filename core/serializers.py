from rest_framework import serializers
from .models import News, AapatKalinSewa


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class AapatKalinSewaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AapatKalinSewa
        fields = "__all__"
