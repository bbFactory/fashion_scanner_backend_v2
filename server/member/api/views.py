from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from server.member.models import Members

from server.member.api.serializers import MemberSerialzier

# Create your views here.


class MemberViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    model = Members
    queryset = Members.objects.all()
    serialzier_class = MemberSerialzier
