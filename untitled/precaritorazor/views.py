from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import AidSerializer, OrganizationSerializer, TypeSerializer, CategorySerializer, CriteriaSerializer
from .models import Aid, Organization, Category, Criteria, Type


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

