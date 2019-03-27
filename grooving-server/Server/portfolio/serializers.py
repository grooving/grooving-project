from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Grooving.models import Portfolio, Calendar, ArtisticGender, PortfolioModule, Zone, PaymentPackage


class CalendarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calendar
        fields = ('year', 'days')


class ArtisticGenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtisticGender
        fields = ('id', 'name', 'parentGender')


class ZoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zone
        fields = ('name', 'parentZone')


class PaymentPackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentPackage
        fields = ('id', 'description')


class PortfolioModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioModule
        fields = ('type', 'link')


class PortfolioSerializer(serializers.ModelSerializer):

    calendar_set = CalendarSerializer(read_only=True, many=True)
    artisticGender = ArtisticGenderSerializer(many=True, read_only=True)
    portfolioModule_set = PortfolioModuleSerializer(many=True, read_only=True)
    zone = ZoneSerializer(read_only=True, many=True)
    paymentPackage_set = PaymentPackageSerializer(read_only=True, many=True)

    class Meta:

        model = Portfolio
        fields = ('artisticName', 'banner', 'calendar_set', 'artisticGender', 'portfolioModule_set', 'zone', 'paymentPackage_set')


class ShortPortfolioSerializer(serializers.ModelSerializer):

    artisticGender = ArtisticGenderSerializer(read_only=True, many=True)

    class Meta:

        model = Portfolio
        fields = ('artisticName', 'artisticGender')


