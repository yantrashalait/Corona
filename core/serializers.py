from rest_framework import serializers
from .models import News, AapatKalinSewa, Numbers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class AapatKalinSewaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AapatKalinSewa
        fields = "__all__"


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = "__all__"
