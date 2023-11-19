from django.shortcuts import render
from models import Customer
from serializers import CustomerSerializer
from rest_framework import generics


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = Customer
