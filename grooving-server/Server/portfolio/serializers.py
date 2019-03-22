from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Grooving.models import Portfolio,Calendar,ArtisticGender,PortfolioModule,Zone,PaymentPackage


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

    calendar = CalendarSerializer(read_only=True)
    artisticGender = ArtisticGenderSerializer(many=True, read_only=True)
    portfolioModule = PortfolioModuleSerializer(many=True, read_only=True)
    zone = ZoneSerializer(read_only=True, many=True)
    hiring = PaymentPackageSerializer(read_only=True)

    class Meta:

        model = Portfolio
        fields = ('artisticName', 'calendar', 'artisticGender', 'portfolioModule', 'zone', 'hiring')



