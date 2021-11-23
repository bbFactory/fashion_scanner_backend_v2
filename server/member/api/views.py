from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from server.member.models import Members
from server.common.models import Color
from server.cloth.api.serializers import KoClothSerializer, EnClothSerializer
from rest_framework.decorators import action
from server.member.api.serializers import KoMemberSerialzier, EnMemberSerialzier
from rest_framework.response import Response
from server.cloth.models import Clothes

# Create your views here.


class MemberViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    model = Members
    queryset = Members.objects.all()
    serialzier_class = [KoMemberSerialzier, EnMemberSerialzier]

    @action(
        detail=False,
        methods=["GET"],
        permission_classes=[AllowAny],
        url_path="info",
    )
    def get_member(self, request, *args, **kwagrs):
        result = {"data": {"ko": {}, "en": {}}}
        ko_member_name = request.GET.get("ko_name")
        en_member_name = request.GET.get("en_name")
        member_info = Members.objects.filter(
            ko_name=ko_member_name
        ) | Members.objects.filter(
            en_name=en_member_name.upper() if en_member_name else en_member_name
        )

        member_info = member_info.first()
        # member_info가 받아오는 값
        # name, group_type, color_id
        ko_member_serializer = KoMemberSerialzier(member_info).data
        en_member_serializer = EnMemberSerialzier(member_info).data

        # color 받아오기
        color = Color.objects.get(id=member_info.color_id).hex_code

        # clothes 받아오기
        clothes = Clothes.objects.filter(member_id=member_info.id)
        ko_cloth_serialzier = KoClothSerializer(clothes, many=True).data
        en_cloth_serialzier = EnClothSerializer(clothes, many=True).data

        result["data"]["ko"]["member"] = ko_member_serializer
        result["data"]["ko"]["color"] = color
        result["data"]["ko"]["clothes"] = ko_cloth_serialzier
    
        result["data"]["en"]["member"] = en_member_serializer
        result["data"]["en"]["color"] = color
        result["data"]["en"]["clothes"] = en_cloth_serialzier

        return Response(result, status=status.HTTP_200_OK)
