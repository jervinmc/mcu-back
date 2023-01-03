from rest_framework import serializers
from .models import Reset

class ResetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reset
        fields="__all__"
