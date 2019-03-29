from django.shortcuts import render
from django.shortcuts import redirect, render
from Grooving.models import Portfolio, Artist
from django.contrib import messages
from django.db.utils import IntegrityError


from django.core.exceptions import PermissionDenied
from utils.authentication_utils import get_logged_user,get_user_type,is_user_authenticated
from rest_framework.response import Response
from django.shortcuts import render_to_response
from rest_framework import generics
from .serializers import PortfolioSerializer
from rest_framework import status
from django.http import Http404


class PortfolioManager(generics.RetrieveUpdateDestroyAPIView):

    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def get_object(self, pk):
        try:
            return Portfolio.objects.get(pk=pk)
        except Portfolio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        portfolio = self.get_object(pk)
        serializer = PortfolioSerializer(portfolio)
        return Response(serializer.data)

    def put(self, request, pk):
        portfolio = self.get_object(pk)
        loggedUser = get_logged_user(request)
        artist = Artist.objects.filter(portfolio=portfolio).first()
        if loggedUser is not None and loggedUser.id == artist.id:
            serializer = PortfolioSerializer(portfolio, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise PermissionDenied("The portfolio is not yours")

    def delete(self, request, pk, format=None):
        portfolio = self.get_object(pk)
        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


