from collections import defaultdict

from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField
from enum import Enum


# Create your models here.


class Actor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        abstract = True


class UserAbstract(Actor):
    photo = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    iban = models.CharField(max_length=255, blank=True, null=True)
    paypalAccount = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True


class CreditCardField:
    holder = models.CharField(max_length=255, blank=False, null=False)
    expirationDate = models.DateField(blank=False, null=False)
    number = models.CharField(blank=False, null=False, max_length=16)
    cvv = models.CharField(blank=False, null=False, max_length=3)

    def __init__(self, holder, expirationDate, number, cvv):
        self.holder = str(holder)
        self.expirationDate = expirationDate
        self.number = number
        self.cvv = cvv


class Customer(UserAbstract):
    creditCard = CreditCardField

    def __str__(self):
        return self.username


class Calendar(models.Model):
    year = models.IntegerField(null=False, validators=[MinValueValidator(2019), MaxValueValidator(3000)])
    days = ArrayField(models.BooleanField(default=False), size=366)

    def __str__(self):
        return self.year


class ArtisticGender(models.Model):
    name = models.CharField(blank=False, null=False, max_length=140)
    parentGender = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Zone(models.Model):
    name = models.CharField(blank=False, null=False, max_length=140)
    parentZone = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PaymentPackage(models.Model):
    description = models.TextField(blank=True, null=True)
    appliedVAT = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('00.0'))])

    def __str__(self):
        return self.description + ' - ' + self.appliedVAT


class Portfolio(models.Model):
    artisticName = models.CharField(blank=True, null=True, max_length=140)
    calendar = models.ForeignKey(Calendar, blank=True, null=True, on_delete=models.CASCADE)
    artisticGender = models.ManyToManyField(ArtisticGender, blank=True, null=True)
    portfolioModule = models.ManyToManyField('PortfolioModule', blank=True, null=True)
    zone = models.ManyToManyField(Zone, blank=True, null=True)
    hiring = models.ForeignKey(PaymentPackage, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.artisticName


ModuleTypeField = (
    ('PHOTO', 'PHOTO'),
    ('DESCRIPTION', 'DESCRIPTION'),
    ('VIDEO', 'VIDEO'),
    ('AUDIO', 'AUDIO'),
    ('SOCIAL', 'SOCIAL'),
    ('MEMBER', 'MEMBER'))


class Artist(UserAbstract):
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE)


class PortfolioModule(models.Model):
    type = models.CharField(max_length=255, choices=ModuleTypeField)
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    portfolio = Portfolio

    def __str__(self):
        return self.type + ' - ' + self.description


class MoneyField:
    amount = models.DecimalField(blank=False, null=False, validators=[MinValueValidator(Decimal('0.0'))])
    currency = models.CharField(blank=False, null=False, default='EUR', max_length=3)

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency


class Performance(PaymentPackage):
    info = models.TextField(blank=False, null=False)
    hours = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('00.5'))])
    price = MoneyField


class Fare(PaymentPackage):
    priceHour = MoneyField


class Custom(PaymentPackage):
    minimumPrice = MoneyField


class SystemConfiguration(models.Model):
    minimumPrice = MoneyField
    paypalTax = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('00.0'))])
    creditCardTax = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('00.0'))])
    vat = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('00.0'))])
    profit = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('00.0'))])
    corporateEmail = models.EmailField
    reportEmail = models.EmailField
    logo = models.CharField(max_length=255, blank=False, null=False)
    appName = models.CharField(max_length=255, blank=False, null=False)
    slogan = models.CharField(max_length=255, blank=True, null=True)
    termsText = models.TextField(blank=False, null=True)
    privacyText = models.TextField(blank=False, null=True)


class EventLocation(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    equipment = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


OfferStatusField =(
    ('PENDING', "PENDING"),
    ('NEGOTIATION', "NEGOTIATION"),
    ('CONTRACT_MADE', "CONTRACT_MADE"),
    ('WITHDRAWN', "WITHDRAWN"),
    ('REJECTED', "REJECTED"),
    ('CANCELED', "CANCELED"),
    ('PAYMENT_MADE', "PAYMENT_MADE"))


class Offer(models.Model):
    description = models.TextField(blank=False, null=False)
    status = models.CharField(max_length=20, choices=OfferStatusField)
    date = models.DateTimeField(null=False, blank=False)
    hours = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('0.5'))])
    price = MoneyField
    paymentCode = models.CharField(max_length=140)
    paymentPackage = models.OneToOneField(PaymentPackage, on_delete=models.CASCADE)
    eventLocation = models.ForeignKey(EventLocation, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
