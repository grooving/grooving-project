from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.postgres.fields import ArrayField

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


class Customer(models.Model):
    user = models.OneToOneField(UserAbstract, blank=False, null=False, on_delete=models.CASCADE)
    creditCard =
    def __str__(self):
        return self.user.actor.username

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
