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
    phone = models.CharField(max_length=255, blank=True, null=True)
    iban = models.CharField(max_length=255, blank=True, null=True)
    paypalAccount = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True



class Customer(UserAbstract):
    #creditcard
    holder = models.CharField(max_length=255, blank=False, null=False)
    expirationDate = models.DateField(blank=False, null=False)
    number = models.CharField(blank=False, null=False, max_length=16)
    cvv = models.CharField(blank=False, null=False, max_length=3)


class ArtisticGender(AbstractEntity):
    name = models.CharField(blank=False, null=False, max_length=140)
    parentGender = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Zone(AbstractEntity):
    name = models.CharField(blank=False, null=False, max_length=140)
    parentZone = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Portfolio(AbstractEntity):
    artisticName = models.CharField(blank=True, null=True, max_length=140)
    artisticGender = models.ManyToManyField(ArtisticGender, blank=True)
    zone = models.ManyToManyField(Zone, blank=True)

    def __str__(self):
        return str(self.artisticName)


class Calendar(AbstractEntity):
    year = models.IntegerField(null=False, validators=[MinValueValidator(2019), MaxValueValidator(3000)])
    days = ArrayField(models.BooleanField(default=False), size=366)
    portfolio = models.ForeignKey(Portfolio, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.year)


class Artist(UserAbstract):
    portfolio = models.OneToOneField(Portfolio, null=True, on_delete=models.CASCADE)
    pass


class Artist(UserAbstract):
    portfolio = models.OneToOneField(Portfolio,null=True,on_delete=models.SET_NULL)
    pass

ModuleTypeField = (
    ('PHOTO', 'PHOTO'),
    ('DESCRIPTION', 'DESCRIPTION'),
    ('VIDEO', 'VIDEO'),
    ('AUDIO', 'AUDIO'),
    ('SOCIAL', 'SOCIAL'),
    ('MEMBER', 'MEMBER'))


class PortfolioModule(AbstractEntity):
    type = models.CharField(max_length=255, choices=ModuleTypeField)
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    portfolioModule = models.ForeignKey(Portfolio, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.type) + ' - ' + str(self.description)


class Performance(AbstractEntity):
    info = models.TextField(blank=False, null=False)
    hours = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(Decimal('00.5'))])
    price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.0'))])
    currency = models.CharField(blank=False, null=False, default='EUR', max_length=3)


class Fare(AbstractEntity):
    priceHour = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.0'))])
    currency = models.CharField(blank=False, null=False, default='EUR', max_length=3)


class Custom(AbstractEntity):
    minimumPrice = models.DecimalField(default=0.0, max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.0'))])
    currency = models.CharField(blank=False, null=False, default='EUR', max_length=3)


class PaymentPackage(AbstractEntity):
    description = models.TextField(blank=True, null=True)
    appliedVAT = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('00.0'))])
    portfolio = models.ForeignKey(Portfolio, blank=True, null=True, on_delete=models.SET_NULL)
    performance = models.OneToOneField(Performance, blank=True, null=True, on_delete=models.SET_NULL)
    fare = models.OneToOneField(Fare, blank=True, null=True, on_delete=models.SET_NULL)
    custom = models.OneToOneField(Custom, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.description) + ' - ' + str(self.appliedVAT)


class SystemConfiguration(AbstractEntity):
    minimumPrice = models.DecimalField(default=0.0, max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.0'))])
    currency = models.CharField(blank=False, null=False, default='EUR', max_length=3)

    paypalTax = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('00.0'))])
    creditCardTax = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('00.0'))])
    vat = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('00.0'))])
    profit = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('00.0'))])
    corporateEmail = models.EmailField
    reportEmail = models.EmailField
    logo = models.CharField(max_length=255, blank=False, null=False)
    appName = models.CharField(max_length=255, blank=False, null=False)
    slogan = models.CharField(max_length=255, blank=True, null=True)
    termsText = models.TextField(blank=False, null=True)
    privacyText = models.TextField(blank=False, null=True)


class EventLocation(AbstractEntity):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=False, null=False)
    equipment = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)


OfferStatusField =(
    ('PENDING', "PENDING"),
    ('NEGOTIATION', "NEGOTIATION"),
    ('CONTRACT_MADE', "CONTRACT_MADE"),
    ('WITHDRAWN', "WITHDRAWN"),
    ('REJECTED', "REJECTED"),
    ('CANCELED', "CANCELED"),
    ('PAYMENT_MADE', "PAYMENT_MADE"))


class Offer(AbstractEntity):
    description = models.TextField(blank=False, null=False)
    status = models.CharField(max_length=20, choices=OfferStatusField)
    date = models.DateTimeField(null=False, blank=False)
    hours = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2, validators=[MinValueValidator(Decimal('0.5'))])
    price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.0'))])
    currency = models.CharField(blank=False, null=False, default='EUR', max_length=3)
    paymentCode = models.CharField(max_length=140, unique=True)
    paymentPackage = models.OneToOneField(PaymentPackage, blank=True, null=True, on_delete=models.SET_NULL)
    eventLocation = models.ForeignKey(EventLocation, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.description)
