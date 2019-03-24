from Grooving.models import Artist, ArtisticGender
from rest_framework import viewsets
from .serializers import ListArtistSerializer
from django.shortcuts import get_object_or_404


class ListArtist(viewsets.ModelViewSet):
    model = Artist
    serializer_class = ListArtistSerializer

    def get_queryset(self):

        artisticname = self.request.query_params.get('artisticName')
        artisticgender = self.request.query_params.get('artisticGender')
        if artisticname or artisticgender:
            if artisticname:
                queryset = Artist.objects.filter(portfolio__artisticName=artisticname)
            if artisticgender:
                artgen = get_object_or_404(ArtisticGender.objects, name=artisticgender)

                if artisticname:
                    queryset = queryset.filter(portfolio__artisticGender=artgen)
                else:
                    queryset = Artist.objects.filter(portfolio__artisticGender=artgen)
        else:
            queryset = Artist.objects.all()
        return queryset
