import json
from rest_framework import serializers
from server.cloth.models import Clothes, Attribute
from server.common.models import Color


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ["ko_name"]


class KoClothSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField("get_category_name")
    attributes = serializers.SerializerMethodField("get_attribute_name")

    class Meta:
        model = Clothes
        fields = [
            "image",
            "category_name",
            "attributes"
        ]

    def get_category_name(self, obj):
        return obj.category.ko_name

    def get_attribute_name(self, obj):
        return [attribute.ko_name for attribute in obj.attributes.all()]


class EnClothSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField("get_en_category_name")
    attributes = serializers.SerializerMethodField("get_en_attribute_name")

    class Meta:
        model = Clothes
        fields = [
            "image",
            "category_name",
            "attributes",
        ]

    def get_en_category_name(self, obj):
        return obj.category.en_name

    def get_en_attribute_name(self, obj):
        return [attribute.en_name.replace("_", " ").title() for attribute in obj.attributes.all()]
