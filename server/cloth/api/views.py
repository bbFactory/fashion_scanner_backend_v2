from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from server.cloth.models import Clothes

from server.cloth.api.serializers import ClothSerializer

# Create your views here.


class ClothViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    model = Clothes
    queryset = Clothes.objects.all()
    serialzier_class = ClothSerializer
