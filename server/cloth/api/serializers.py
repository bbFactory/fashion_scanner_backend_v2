import json
from rest_framework import serializers
from server.cloth.models import Clothes


class ClothSerialzier(serializers.Serializer):
    class Meta:
        model = Clothes
        fields = "__all__"
