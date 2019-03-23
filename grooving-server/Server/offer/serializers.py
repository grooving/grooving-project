from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Grooving.models import Offer, PaymentPackage


class PaymentPackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentPackage
        fields = ('id', 'description')


class OfferSerializer(serializers.ModelSerializer):
    paymentpackage_set = PaymentPackageSerializer(read_only=True, many=False)

    class Meta:
        model = Offer
        fields = ('description', 'status', 'date', 'hours', 'paymentpackage_set', 'eventLocation_id')

