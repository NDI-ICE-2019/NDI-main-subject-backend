from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import AidSerializer
from .models import Aid


class AidViewSet(viewsets.ModelViewSet):
    queryset = Aid.objects.all().order_by('title')
    serializer_class = AidSerializer

