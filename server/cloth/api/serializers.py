import json
from rest_framework import serializers
from server.cloth.models import Clothes, Attribute
from server.common.models import Color


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ["ko_name"]


class ClothSerializer(serializers.ModelSerializer):
    color_name = serializers.SerializerMethodField("get_color_name")
    ko_category_name = serializers.SerializerMethodField("get_category_name")
    en_category_name = serializers.SerializerMethodField("get_en_category_name")
    attributes = serializers.SerializerMethodField("get_attribute_name")
    en_attributes = serializers.SerializerMethodField("get_en_attribute_name")

    class Meta:
        model = Clothes
        fields = [
            "id",
            "image",
            "color_name",
            # "category_id",
            "ko_category_name",
            "en_category_name",
            "attributes",
            "en_attributes",
            # "ko_attribute",
            # "en_attribute_list",
        ]

    def get_color_name(self, obj):
        return obj.color.hex_code

    def get_category_name(self, obj):
        return obj.category.ko_name

    def get_attribute_name(self, obj):
        return [attribute.ko_name for attribute in obj.attributes.all()]

    def get_en_category_name(self, obj):
        return obj.category.en_name

    def get_en_attribute_name(self, obj):
        return [attribute.en_name for attribute in obj.attributes.all()]
