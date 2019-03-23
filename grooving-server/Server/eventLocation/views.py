from django.shortcuts import render
from django.shortcuts import redirect, render
from Grooving.models import EventLocation
from django.contrib import messages
from django.db.utils import IntegrityError

from rest_framework.response import Response
from django.shortcuts import render_to_response
from rest_framework import generics
from .serializers import EventLocationSerializer
from rest_framework import status
from django.http import Http404
# Create your views here.

class EventLocationManager(generics.RetrieveUpdateDestroyAPIView):

    queryset = EventLocation.objects.all()
    serializer_class = EventLocationSerializer

    def get_object(self, pk):
        try:
            return EventLocation.objects.get(pk=pk)
        except EventLocation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        eventLocation = self.get_object(pk)
        serializer = EventLocationSerializer(eventLocation)
        return Response(serializer.data)

    def post(self, request, pk, **kwargs):
        eventLocation = self.get_object(pk)
        serializer = EventLocationSerializer(eventLocation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        eventLocation = self.get_object(pk)
        if len(request.data) == 1 and 'status' in request.data:
            serializer = EventLocationSerializer(eventLocation, data=request.data, partial=True)

        else:
            serializer = EventLocationSerializer(eventLocation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        eventLocation = self.get_object(pk)
        eventLocation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object(pk)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

