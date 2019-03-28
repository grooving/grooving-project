from django.shortcuts import render
from django.shortcuts import redirect, render
from Grooving.models import ArtisticGender
from django.contrib import messages
from django.db.utils import IntegrityError

from rest_framework.response import Response
from django.shortcuts import render_to_response
from rest_framework import generics
from .serializers import ArtisticGenderSerializer
from rest_framework import status
from django.http import Http404


class ArtisticGenderManager(generics.RetrieveUpdateDestroyAPIView):

    queryset = ArtisticGender.objects.all()
    serializer_class = ArtisticGenderSerializer

    def get_object(self, pk):
        try:
            return ArtisticGender.objects.get(pk=pk)
        except ArtisticGender.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        portfolio = self.get_object(pk)
        serializer = ArtisticGenderSerializer(portfolio)
        return Response(serializer.data)

    def put(self, request, pk):
        artisticGender = self.get_object(pk)
        if len(request.data) == 1 and 'status' in request.data:
            serializer = ArtisticGenderSerializer(artisticGender, data=request.data, partial=True)

        else:
            serializer = ArtisticGenderSerializer(artisticGender, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        artisticGender = self.get_object(pk)
        artisticGender.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object(pk)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)


class CreateArtisticGender(generics.CreateAPIView):
    queryset = ArtisticGender.objects.all()
    serializer_class = ArtisticGenderSerializer

    def post(self, request, *args, **kwargs):
        serializer = ArtisticGenderSerializer(data=request.data, partial=True)
        if serializer.validate(request.data):
            serializer.is_valid()
            artisticGender = serializer.save()
            serialized = ArtisticGenderSerializer(artisticGender)
            return Response(serialized.data, status=status.HTTP_201_CREATED)
