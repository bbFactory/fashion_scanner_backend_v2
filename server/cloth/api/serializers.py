import json
from rest_framework import serializers
from server.cloth.models import Clothes, Attribute
from server.common.models import Color


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ["ko_name"]


class ClothSerialzier(serializers.ModelSerializer):
    color_name = serializers.SerializerMethodField("get_color_name")
    category_name = serializers.SerializerMethodField("get_category_name")
    attribute_list = serializers.SerializerMethodField("get_attribute_name")
    # image_url = serializers.SerializerMethodField("get_image_url")

    class Meta:
        model = Clothes
        fields = [
            "id",
            # "image_url",
            "color_name",
            # "category_id",
            "category_name",
            # "attributes",
            "attribute_list",
        ]

    def get_color_name(self, obj):
        return obj.color.hex_code

    def get_category_name(self, obj):
        return obj.category.ko_name

    def get_attribute_name(self, obj):
        return [attribute.ko_name for attribute in obj.attributes.all()]
