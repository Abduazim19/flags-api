from django.shortcuts import render
# flags/views.py
from rest_framework import viewsets
from .models import Flag
from .serializers import FlagSerializer

class FlagViewSet(viewsets.ModelViewSet):
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer

# Create your views here.
