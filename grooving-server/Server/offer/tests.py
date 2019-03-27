from Grooving.models import Offer, Customer, Artist, Portfolio, User, Calendar, PaymentPackage
from Grooving.models import EventLocation, Zone, Performance
from django.utils import timezone

from rest_framework.test import APITestCase

# Create your tests here.


class OfferTestCase(APITestCase):

    def test_accept_offer(self):

        user1 = User.objects.create(username="pedro", email="pedro@pedro.com", password="pedro")
        user1.save()
        customer1 = Customer.objects.create(user=user1,phone="959959959", photo="www.google.png",
                                            iban="DE89 3704 0044 0532 0130 00")
        customer1.save()

        days = [True] * 366

        user2 = User.objects.create(username="artist", email="artist@artist.com", password="artist")
        user2.save()

        zone1 = Zone.objects.create(name="Sevilla Sur")
        zone1.save()
        event_location1 = EventLocation.objects.create(name="Sala Rajoy", address="C/Madrid",
                                                       equipment="Speakers and microphone",
                                                       description="The best event location", zone=zone1)
        event_location1.save()

        portfolio1 = Portfolio.objects.create(artisticName="Juanartist")
        portfolio1.zone.add(zone1)
        portfolio1.save()

        artist1 = Artist.objects.create(portfolio=portfolio1, user=user2, phone="888888888",
                                        photo="www.google.png", iban="DE89 3704 0044 0532 0130 00")
        artist1.save()
        performance1 = Performance.objects.create(info="info", hours=3, price=200.0, currency="EUR")
        performance1.save()
        payment_package1 = PaymentPackage.objects.create(description="Paymentcription", appliedVAT="0.35",
                                                         portfolio=portfolio1, performance=performance1)

        payment_package1.save()

        calendar1 = Calendar.objects.create(year=2019, days=days, portfolio=portfolio1)
        calendar1.save()

        date = timezone.now()

        offer1 = Offer.objects.create(description="DESCRIPTIONOFFER1", status='PENDING', date=date, price="200",currency="EUR", hours=2,
                                      paymentCode='EEE', eventLocation=event_location1, paymentPackage=payment_package1)
        offer1.save()
        data1 = {"username": "artist", "password": "artist"}
        self.client.post("/api/login/", data1, format='json')

        data = {"status": "CONTRACT_MADE"}
        response = self.client.put('/offer/1/', data, format='json')
        self.assertEqual(response.status_code, 200)
        print(response)
        self.client.logout()
