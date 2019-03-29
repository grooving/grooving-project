from Grooving.models import Offer, Artist, Portfolio, User, Calendar, PaymentPackage, Customer
from Grooving.models import EventLocation, Zone, Performance, ArtisticGender
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
import datetime
import pytz


class ArtistGenderTestCase(APITestCase):

    def test_manage_artistGender_artist(self):

        days = ['2019-06-02', '2019-08-02', '2019-10-15', '2019-11-02']
        date = datetime.datetime(2020,2,7,8,49,56,81433, pytz.UTC)

        user1_artist1 = User.objects.create(username='artist1', password=make_password('artist1artist1'),
                                            first_name='Cdds', last_name='Pedro',
                                            email='artist1@gmail.com')
        user1_artist1.save()

        zone1 = Zone.objects.create(name="Sevilla Sur")
        zone1.save()

        artisticGender = ArtisticGender.objects.create(name="Rock")
        artisticGender.save()

        portfolio1 = Portfolio.objects.create(artisticName="Juanartist")
        portfolio1.zone.add(zone1)
        portfolio1.save()

        artist1 = Artist.objects.create(user=user1_artist1, portfolio=portfolio1, phone='600304999')
        artist1.save()

        performance1 = Performance.objects.create(info="info", hours=3, price=200.0, currency="EUR")
        performance1.save()
        payment_package1 = PaymentPackage.objects.create(description="Paymentcription", appliedVAT="0.35",
                                                         portfolio=portfolio1, performance=performance1)

        payment_package1.save()

        calendar1 = Calendar.objects.create(days=days, portfolio=portfolio1)
        calendar1.save()

        data1 = {"username": "artist1", "password": "artist1artist1"}
        response = self.client.post("/api/login/", data1, format='json')

        token_num = response.get('x-auth')
        token = Token.objects.all().filter(pk=token_num).first()
        print(token.key)
        self.assertEqual(response.status_code, 200)

        data = {"id": "" + str(zone1.id), "name": "Cadiz", "portfolio_set": [str(portfolio1.id)]}

        response1 = self.client.put('/zone/{}/'.format(zone1.id), data, format='json',
                                    HTTP_AUTHORIZATION='Token '+token.key)
        self.assertEqual(response1.status_code, 200)

        print(response1)
        print(ArtisticGender.objects.filter(pk=artisticGender.id).first())
