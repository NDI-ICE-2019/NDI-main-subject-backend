from rest_framework import serializers

from .models import Aid, Organization, Criteria, Category, Type
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aid
        fields = "__all__"


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CriteriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Criteria
        fields = "__all__"

