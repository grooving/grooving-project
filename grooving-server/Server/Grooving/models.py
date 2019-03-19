from collections import defaultdict

from django.contrib.auth.models import User
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.postgres.fields import ArrayField
from enum import Enum


# Create your models here.

class Actor(AbstractUser):

    email = models.EmailField(blank=False, null=False, unique=True)

    class Meta:
        abstract=True

class User(Actor):
    photo = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    iban = models.CharField(blank=True, null=True)
    paypalAccount = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.username


class Artist(models.Model):
    user = User(blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

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
    user = User(blank=False, null=False, on_delete=models.CASCADE)
    creditCard =

    def __str__(self):
        return self.username


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

class ModuleTypeField(Enum):
    PHOTO = 'PHOTO'
    DESCRIPTION = 'DESCRIPTION'
    VIDEO = 'VIDEO'
    AUDIO = 'AUDIO'
    SOCIAL = 'SOCIAL'
    MEMBER = 'MEMBER'

class PortfolioModule(models.Model):
    type = models.CharField(choices=[(tag, tag.value) for tag in ModuleTypeField])
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    portfolio = Portfolio(blank=False, null=False)

    def __str__(self):
        return self.type + ' - ' + self.description

class PaymentPackage(models.Model):
   description = models.TextField(blank=True, null=True)
   appliedVAT = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('00.0'))])

   def __str__(self):
       return self.description + ' - ' + self.appliedVAT

   class Meta:
       abstract=True

class MoneyField:

    amount = models.DecimalField(blank=False, null=False, validators=[MinValueValidator(Decimal('0.0'))])
    currency = models.CharField(blank=False, null=False, default='EUR', max_length=3)

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

class Performance(PaymentPackage):
    info = models.TextField(blank=False, null=False)
    hours = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('00.5'))])
    price = MoneyField(black=False, null=False)

class Fare(PaymentPackage):
    priceHour = MoneyField(black=False, null=False)

class Custom(PaymentPackage):
    minimumPrice = MoneyField(black=False, null=False)

class SystemConfiguration(models.Model):
    minimumPrice = MoneyField(black=False, null=False)
    paypalTax = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('00.0'))])
    creditCardTax = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('00.0'))])
    vat = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('00.0'))])
    profit = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('00.0'))])
    corporateEmail = models.EmailField(blank=False, null=False)
    reportEmail = models.EmailField(blank=False, null=False)
    logo = models.CharField(blank=False, null=False)
    appName = models.CharField(blank=False, null=False)
    slogan = models.CharField(blank=True, null=True)
    termsText = models.TextField(blank=False, null=True)
    privacyText = models.TextField(blank=False, null=True)

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
