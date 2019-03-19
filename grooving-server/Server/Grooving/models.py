from django.contrib.auth.models import User
from decimal import Decimal
from django.db import models
from enum import Enum
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.postgres.fields import ArrayField

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


class Customer(models.Model):
    user = User(blank=False, null=False, on_delete=models.CASCADE)
    creditCard =

    def __str__(self):
        return self.username

class Calendar(models.Model):
    year = models.IntegerField(null=False, validators=[MinValueValidator(2019), MaxValueValidator(3000)])
    days = ArrayField(models.IntegerField(),size=)

    def __str__(self):
        return self.year

class Portfolio(models.Model):
    artisticName = models.CharField(blank=True, null=True, max_length=140)
    calendar =  models.OneToManyField(Calendar, blank=True, null=True, on_delete=models.CASCADE)
    artisticGender =  models.ManyToManyField(ArtisticGender, blank=True, null=True, on_delete=models.CASCADE)
    portfolioModule =  models.ManyToManyField(PortfolioModule, blank=True, null=True, on_delete=models.CASCADE)
    zone =  models.ManyToManyField(Zone, blank=True, null=True, on_delete=models.CASCADE)
    hiring =  models.OneToManyField(Hiring, blank=True, null=True, on_delete=models.CASCADE)

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
