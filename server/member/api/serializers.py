from django.shortcuts import render

# Create your views here.
import json
from rest_framework import serializers
from server.member.models import Members


class KoMemberSerialzier(serializers.ModelSerializer):
    name = serializers.SerializerMethodField("get_ko_name")
    group_type = serializers.SerializerMethodField("get_group_type")

    class Meta:
        model = Members
        fields = [
            "name",
            "group_type",
        ]
    
    def get_ko_name(self, obj):
        return obj.ko_name

    def get_group_type(self, obj):
        return obj.group_type.capitalize()


class EnMemberSerialzier(serializers.ModelSerializer):
    name = serializers.SerializerMethodField("get_en_name")
    group_type = serializers.SerializerMethodField("get_group_type")
    
    class Meta:
        model = Members
        fields = [
            "name",
            "group_type",
        ]
    
    def get_en_name(self, obj):
        return obj.en_name.capitalize()
    
    def get_group_type(self, obj):
        return obj.group_type.capitalize()

    