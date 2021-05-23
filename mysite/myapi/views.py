from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import AdvisorSerializer
from .models import Advisor


class AdvisorViewSet(viewsets.ModelViewSet):
    queryset = Advisor.objects.all().order_by('name')
    serializer_class = AdvisorSerializer
