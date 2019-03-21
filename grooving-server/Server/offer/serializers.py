from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Grooving.models import Offer


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

