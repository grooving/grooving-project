from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Grooving.models import Artist
from user.serializers import UserSerializer


class ArtistInfoSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        depth = 1
        model = Artist
        fields = ('id', 'user', 'photo', 'phone', 'iban', 'paypalAccount')
