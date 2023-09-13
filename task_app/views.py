from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

class CreatePersonView(generics.ListCreateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer


class RetrieveUpdatePersonView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    lookup_field='pk'


