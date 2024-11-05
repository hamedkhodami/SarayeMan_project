from rest_framework import serializers
from .models import PropertyModel


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyModel
        fields = '__all__'
