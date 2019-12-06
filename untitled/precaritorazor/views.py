from django.http import HttpResponse

from rest_framework import viewsets
from django.contrib.auth.models import User, Group

from .serializers import AidSerializer, OrganizationSerializer, TypeSerializer, CategorySerializer, CriteriaSerializer
from .models import Aid, Organization, Category, Criteria, Type

from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AidViewSet(viewsets.ModelViewSet):
    queryset = Aid.objects.all().order_by('title')
    serializer_class = AidSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by('name')
    serializer_class = OrganizationSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CriteriaViewSet(viewsets.ModelViewSet):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer

