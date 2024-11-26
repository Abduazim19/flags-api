# flags/serializers.py
from rest_framework import serializers
from .models import Flag

class FlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flag
        fields = ['id', 'image', 'country_name']
