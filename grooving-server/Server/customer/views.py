from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import CustomerInfoSerializer
from django.core.exceptions import PermissionDenied
from Grooving.models import Customer


class GetPersonalInformationCustomer(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CustomerInfoSerializer
    queryset = []

    def get_queryset(self):

        if self.request.user.is_authenticated:
            loggeduser = self.request.user
            queryset = Customer.objects.filter(user=loggeduser)
            return queryset
        else:
            raise PermissionDenied()
