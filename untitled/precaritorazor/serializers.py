from rest_framework import serializers

from .models import Aid


class AidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aid
        fields = ('title', 'description')

