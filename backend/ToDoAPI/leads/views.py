from django.shortcuts import render
from rest_framework import generics

from leads.models import Leads
from leads.serializers import LeadSerializer

# Create your views here.
class LeadListCreate(generics.ListCreateAPIView):
  queryset = Leads.objects.all()
  serializer_class = LeadSerializer
