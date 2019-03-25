from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class AbstractEntity(models.Model):
    creationMoment = models.DateTimeField(auto_now_add=True)
    lastModification = models.DateTimeField(auto_now=True)
    isHidden = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Actor(AbstractEntity):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        abstract = True


class UserAbstract(Actor):
    photo = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    iban = models.CharField(max_length=34, blank=True, null=True)
    paypalAccount = models.EmailField(blank=True, null=True)

    class Meta:
        abstract = True


class ArtisticGender(AbstractEntity):
    name = models.CharField(max_length=140)
    parentGender = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Zone(AbstractEntity):
    name = models.CharField(max_length=140)
    parentZone = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Portfolio(AbstractEntity):
    artisticName = models.CharField(blank=True, null=True, max_length=140)
    portfolioModules = models.ForeignKey('PortfolioModule', blank=True, null=True, on_delete=models.SET_NULL)
    artisticGender = models.ManyToManyField(ArtisticGender)
    zone = models.ManyToManyField(Zone)

    def __str__(self):
        return str(self.artisticName)


class Calendar(AbstractEntity):
    year = models.IntegerField(validators=[MinValueValidator(2019), MaxValueValidator(3000)])
    days = ArrayField(models.BooleanField(default=False), size=366)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.year)


class Artist(UserAbstract):
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE)


ModuleTypeField = (
    ('PHOTO', 'PHOTO'),
    ('DESCRIPTION', 'DESCRIPTION'),
    ('VIDEO', 'VIDEO'),
    ('AUDIO', 'AUDIO'),
    ('SOCIAL', 'SOCIAL'),
    ('MEMBER', 'MEMBER'))


class PortfolioModule(AbstractEntity):
    type = models.CharField(max_length=20, choices=ModuleTypeField)
    link = models.URLField(blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    portfolioModule = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.type) + ' - ' + str(self.description)


class Performance(AbstractEntity):
    info = models.TextField(max_length=255)
    hours = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('0.5'))])
    price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.0'))])
    currency = models.CharField(default='EUR', max_length=3)


class Fare(AbstractEntity):
    priceHour = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.0'))])
    currency = models.CharField(default='EUR', max_length=3)


class Custom(AbstractEntity):
    minimumPrice = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.0'))])
    currency = models.CharField(default='EUR', max_length=3)


class PaymentPackage(AbstractEntity):
    description = models.TextField(blank=True, null=True)
    appliedVAT = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('0.0'))])
    portfolio = models.ForeignKey(Portfolio, on_delete=models.PROTECT)
    performance = models.OneToOneField(Performance, blank=True, null=True, on_delete=models.SET_NULL)
    fare = models.OneToOneField(Fare, blank=True, null=True, on_delete=models.SET_NULL)
    custom = models.OneToOneField(Custom, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.description) + ' - ' + str(self.appliedVAT)


class SystemConfiguration(AbstractEntity):
    minimumPrice = models.DecimalField(default=0.0, max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.0'))])
    currency = models.CharField(default='EUR', max_length=3)
    paypalTax = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('0.0'))])
    creditCardTax = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('0.0'))])
    vat = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('0.0'))])
    profit = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('0.0'))])
    corporateEmail = models.EmailField
    reportEmail = models.EmailField
    logo = models.CharField(max_length=255)
    appName = models.CharField(max_length=255)
    slogan = models.CharField(max_length=255, blank=True, null=True)
    termsText = models.TextField
    privacyText = models.TextField


class EventLocation(AbstractEntity):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255)
    equipment = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name)


class Customer(UserAbstract):
    #creditcard
    holder = models.CharField(max_length=255)
    expirationDate = models.DateField
    number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    eventLocation = models.ForeignKey(EventLocation, blank=True, null=True, on_delete=models.SET_NULL)


OfferStatusField =(
    ('PENDING', "PENDING"),
    ('NEGOTIATION', "NEGOTIATION"),
    ('CONTRACT_MADE', "CONTRACT_MADE"),
    ('WITHDRAWN', "WITHDRAWN"),
    ('REJECTED', "REJECTED"),
    ('CANCELED', "CANCELED"),
    ('PAYMENT_MADE', "PAYMENT_MADE"))


class Offer(AbstractEntity):
    description = models.TextField
    status = models.CharField(max_length=20, choices=OfferStatusField)
    date = models.DateTimeField
    hours = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2, validators=[MinValueValidator(Decimal('0.5'))])
    price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.0'))])
    currency = models.CharField(default='EUR', max_length=3)
    paymentCode = models.CharField(max_length=140, unique=True, null=True, blank=True)
    paymentPackage = models.ForeignKey(PaymentPackage, on_delete=models.PROTECT)
    eventLocation = models.ForeignKey(EventLocation, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.description)
