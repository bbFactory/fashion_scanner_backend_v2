from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from server.member.models import Members
from server.common.models import Color
from rest_framework.decorators import action
from server.member.api.serializers import MemberSerialzier
from rest_framework.response import Response

# Create your views here.


class MemberViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    model = Members
    queryset = Members.objects.all()
    serialzier_class = MemberSerialzier

    @action(detail=False, methods=["GET"], permission_classes=[AllowAny])
    def get_member(self, request, *args, **kwagrs):
        result = {"data": []}
        country_code = request.GET.get("country_code")
        if country_code == "kr":
            member_name = request.GET.get("ko_name")
        else:
            member_name = request.GET.get("en_name")
        member_info = Members.objects.filter(name=member_name)
        # member_info가 받아오는 값
        # member_id, ko_name, en_name, group_type, color_id
        member_serializer = MemberSerialzier(member_info).data
        color = Color.objects.filter(id=member_info.color_id).values("hex_code")
        result["data"].append({"member": member_serializer, "color": color})
        return Response(result, status=status.HTTP_200_OK)
