from django.shortcuts import render

# Create your views here.
import json
from rest_framework import serializers
from server.member.models import Members


class MemberSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = [
            "id",
            "ko_name",
            "en_name",
            "group_type",
        ]
