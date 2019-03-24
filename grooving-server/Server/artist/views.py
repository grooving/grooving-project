from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import ArtistInfoSerializer
from django.core.exceptions import PermissionDenied
from Grooving.models import Artist


class GetPersonalInformation(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ArtistInfoSerializer
    queryset = []

    def get_queryset(self):

        if self.request.user.is_authenticated:
            loggeduser = self.request.user
            queryset = Artist.objects.filter(user=loggeduser)
            return queryset
        else:
            raise PermissionDenied()
