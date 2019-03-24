from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Grooving.models import Offer
from utils.Assertions import assert_true

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
    paymentCode = serializers.CharField(default=None)

    class Meta:
        model = Offer
        fields = ('description', 'status', 'date', 'hours', 'paymentCode', 'paymentPackage_id', 'eventLocation_id')

    # Esto sobrescrive una función heredada del serializer.
    def save(self):
        # Raise exception with True
        self.is_valid(True)
        offer=self.
        print("Clave primaria:"+str(offer.pk))
        # creation
        if offer.pk is None:
            offer = self._service_create(offer)
        # edit
        else:
            offer = self._service_update(offer)

        Offer.objects.save(offer)

    #Se pondrá service delante de nuestros métodos para no sobrescribir por error métodos del serializer
    @staticmethod
    def _service_create(offer):
        offer.status = 'PENDING'
        if offer.paymentPackage.performance is not None:
            offer.hours = offer.paymentPackage.performance.hours
            offer.price = offer.paymentPackage.performance.price
        elif offer.paymentPackage.fare is not None:
            offer.price = offer.paymentPackage.fare.price * offer.hours
        else:
            assert_true(offer.paymentPackage.custom is not None, "Una oferta debe tener un algún paquete")
        # offer.paymentCode = None
        return offer

    @staticmethod
    def _service_update(offer):
        offer_in_db = Offer.objects.filter(pk=offer.pk).first()
        assert_true(offer_in_db, "No existe una oferta con esa id")
        return offer




"""
class CreateOfferRequest(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ('description', 'date', 'hours', 'price', 'paymentPackage_id', 'eventLocation_id')

"""


