from django.shortcuts import render
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from .serializers import ArtistInfoSerializer
from django.core.exceptions import PermissionDenied
from Grooving.models import Artist
from rest_framework.response import Response


class GetPersonalInformationOfArtist(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ArtistInfoSerializer

    def get(self, name):

        if self.request.user.is_authenticated:
            loggeduser = self.request.user
            try:
                queryset = Artist.objects.get(user=loggeduser)
                serializer = ArtistInfoSerializer(queryset)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                raise PermissionDenied()
        else:
            raise PermissionDenied()
