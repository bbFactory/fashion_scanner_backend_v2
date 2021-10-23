from django.shortcuts import render

# Create your views here.
import json
from rest_framework import serializers
from server.member.models import Members


class MemberSerialzier(serializers.Serializer):
    class Meta:
        model = Members
        fields = "__all__"
