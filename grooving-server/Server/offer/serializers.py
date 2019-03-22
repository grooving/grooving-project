from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Grooving.models import Offer


'''class OfferSerializer(serializers.Serializer):
    class Meta:
        model = Offer
        fields = '__all__'

    def create(self, validated_data):
        return Offer(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.date = validated_data.get('date', instance.date)
        instance.hours = validated_data.get('hours', instance.hours)
        instance.paymentCode = validated_data.get('paymentCode', instance.paymentCode)
        instance.eventLocation_id = validated_data.get('eventLocation_id', instance.eventLocation_id)
        instance.paymentPackage_id = validated_data.get('paymentPackage_id', instance.paymentPackage_id)
        return instance
'''

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('description', 'status', 'date', 'hours', 'paymentCode', 'paymentPackage_id', 'eventLocation_id')

