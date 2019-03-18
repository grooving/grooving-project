from collections import defaultdict

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField
from enum import Enum


# Create your models here.
class UserAbstract(models.Model):
    actor = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    photo = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    iban = models.CharField(blank=True, null=True)
    paypalAccount = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.actor.username


class Artist(models.Model):
    user = models.OneToOneField(UserAbstract, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.actor.username

class CreditCardField():
    holder = models.CharField(blank=False, null=False)
    expirationDate = models.DateField(blank=False, null=False, allow_future=True)
    number = models.CharField(blank=False, null=False, max_length=16)
    cvv = models.CharField(blank=False, null=False, max_length=3)

    def __init__(self, holder, expirationDate, number, cvv):
        self.holder = str(holder)
        self.expirationDate = expirationDate
        number = number
        cvv = cvv

class Customer(models.Model):
    user = models.OneToOneField(UserAbstract, blank=False, null=False, on_delete=models.CASCADE)
    creditcard = CreditCardField(blank=True, null=True)

    def __str__(self):
        return self.user.actor.username


class Calendar(models.Model):
    year = models.IntegerField(null=False, validators=[MinValueValidator(2019), MaxValueValidator(3000)])
    days = ArrayField(models.BooleanField(default=False), size=366)

    def __str__(self):
        return self.year


class ArtisticGender(models.Model):
    name = models.CharField(blank=False, null=False, max_length=140)
    parentGender = models.ManyToOneField('self', blank=True, null=True)

    def __str__(self):
        return self.name


class Zone(models.Model):
    name = models.CharField(blank=False, null=False, max_length=140)
    parentZone = models.ManyToOneField('self', blank=True, null=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    artisticName = models.CharField(blank=True, null=True, max_length=140)
    calendar = models.OneToManyField(Calendar, blank=True, null=True, on_delete=models.CASCADE)
    artisticGender = models.ManyToManyField(ArtisticGender, blank=True, null=True, on_delete=models.CASCADE)
    portfolioModule = models.ManyToManyField(PortfolioModule, blank=True, null=True, on_delete=models.CASCADE)
    zone = models.ManyToManyField(Zone, blank=True, null=True, on_delete=models.CASCADE)
    hiring = models.OneToManyField(PaymentPackage, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.artisticName


class EventLocation(models.Model):
    name = models.CharField(blank=False, null=False)
    address = models.CharField(blank=False, null=False)
    equipment = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    zone = models.ManyToOneField(Zone, blank=False, null=False)
    customer = models.ManyToOneField(Customer, blank=True, null=True)

    def __str__(self):
        return self.name


class OfferStatusField(Enum):
    PENDING = "PENDING"
    NEGOTIATION = "NEGOTIATION"
    CONTRACT_MADE = "CONTRACT_MADE"
    WITHDRAWN = "WITHDRAWN"
    REJECTED = "REJECTED"
    CANCELED = "CANCELED"
    PAYMENT_MADE = "PAYMENT_MADE"


class Offer(models.Model):
    description = models.TextField(blank=False, null=False)
    status = models.CharField(language=models.CharField(
        max_length=15,
        choices=[(tag, tag.value) for tag in OfferStatusField]
    ))
    date = models.DateTimeField(null=False, blank=False)
    hours = models.FloatField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    paymentCode = models.CharField(max_length=140)
    paymentPackage = models.OneToOneField(PaymentPackage, blank=False, null=False)
    eventLocation = models.OneToManyField(EventLocation, blank=False, null=False)

    def __str__(self):
        return self.description

