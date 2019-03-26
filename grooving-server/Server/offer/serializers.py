from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Grooving.models import Offer, PaymentPackage, Performance, Fare, Custom


class FareSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Fare
        fields = ('id', 'priceHour', 'currency')


class PerformanceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Performance
        fields = ('id', 'info', 'hours', 'price', 'currency')


class CustomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Custom
        fields = ('id', 'minimumPrice', 'currency')


class PaymentPackageSerializer(serializers.HyperlinkedModelSerializer):
    performance = PerformanceSerializer(read_only=True)
    fare = FareSerializer(read_only=True)
    custom = CustomSerializer(read_only=True)

    class Meta:
        model = PaymentPackage
        fields = ('id', 'description', 'performance', 'fare', 'custom')


class OfferSerializer(serializers.HyperlinkedModelSerializer):

    #paymentCode = PaymentPackageSerializer(read_only=True)

    class Meta:
        model = Offer
        depth = 1
        fields = ('description', 'status', 'date', 'hours')

