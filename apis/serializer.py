from rest_framework import serializers

from .models import GeeksModel


class GeeksSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = GeeksModel
        fields = ('title', 'description')
