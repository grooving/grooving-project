from django.test import TestCase

from Grooving.models import ArtisticGender, Artist, Portfolio, User, PaymentPackage
from datetime import datetime
from rest_framework.test import APITestCase
# Create your tests here.


class ListArtistTestCase(TestCase):

    def test_list_artists(self):

        user = User()
        user.email = "juan@juan.com"
        user.username = "artist"
        user.password= "artist"
        user.id = "43"
        user.save()

        artista = Artist()
        artista.photo = "https://conectandomeconlau.com.co/wp-content/uploads/2018/03/%C2%BFTienes-las-caracteri%CC%81sticas-para-ser-un-Artista.png"
        artista.id ="56"
        artista.iban = "AD1400080001001234567890"
        artista.phone = "999999999"
        artista.paypalAccount = "user=artist,password=artist"
        artista.user_id = "43"
        artista.save()

        response = self.client.get('/artists/'.format(1), format='json')
        self.assertEqual(response.status_code, 200)
        item_dict = response.json()
        self.assertTrue(len(item_dict['results']) == 1)
        print(response)

    def test_list_artists_filter_artistic_name(self):

        user = User()
        user.email = "juan@juan.com"
        user.username = "artist"
        user.password= "artist"
        user.id = "43"
        user.save()

        paymentPackage = PaymentPackage()
        paymentPackage.id = "87"
        paymentPackage.description = "paymentPackage description"
        paymentPackage.appliedVAT = "0.07"
        paymentPackage.save()

        portfolio1 = Portfolio()
        portfolio1.id = "2"
        portfolio1.artisticName = "Jose"
        portfolio1.paymentPackage = paymentPackage
        portfolio1.save()

        artista = Artist()
        artista.photo = "https://conectandomeconlau.com.co/wp-content/uploads/2018/03/%C2%BFTienes-las-caracteri%CC%81sticas-para-ser-un-Artista.png"
        artista.id ="56"
        artista.iban = "AD1400080001001234567890"
        artista.phone = "999999999"
        artista.paypalAccount = "user=artist,password=artist"
        artista.user_id = "43"
        artista.portfolio = portfolio1
        artista.save()

        user2 = User()
        user2.email = "juanjo@juanjo.com"
        user2.username = "artist2"
        user2.password = "artist2"
        user2.id = "44"
        user2.save()

        paymentPackage2 = PaymentPackage()
        paymentPackage2.id = "88"
        paymentPackage2.description = "paymentPackage description 2222222222"
        paymentPackage2.appliedVAT = "0.07"
        paymentPackage2.save()

        portfolio2 = Portfolio()
        portfolio2.id = "3"
        portfolio2.artisticName = "María se fue a la cama a las diez"
        portfolio2.paymentPackage = paymentPackage2
        portfolio2.save()

        artista2 = Artist()
        artista2.photo = "https://conectandomeconlau.com.co/wp-content/uploads/2018/03/%C2%BFTienes-las-caracteri%CC%81sticas-para-ser-un-Artista.png"
        artista2.id = "57"
        artista2.iban = "AD1400080001001234567890"
        artista2.phone = "999999999"
        artista2.paypalAccount = "user=artist,password=artist"
        artista2.user_id = "44"
        artista2.portfolio = portfolio2
        artista2.save()

        response = self.client.get('/artists/?artisticName=Jose', format='json')
        item_dict = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(item_dict['results']) == 1)
        print(response)

    def test_list_artists_filter_artistic_gender(self):

        user = User()
        user.email = "juan@juan.com"
        user.username = "artist"
        user.password= "artist"
        user.id = "43"
        user.save()

        paymentPackage = PaymentPackage()
        paymentPackage.id = "87"
        paymentPackage.description = "paymentPackage description"
        paymentPackage.appliedVAT = "0.07"
        paymentPackage.save()

        artisticGender1 = ArtisticGender()
        artisticGender1.name = "Rock"
        artisticGender1.parentGender = None
        artisticGender1.id = "3"
        artisticGender1.save()

        portfolio1 = Portfolio()
        portfolio1.id = "2"
        portfolio1.artisticName = "Jose"
        portfolio1.paymentPackage = paymentPackage
        portfolio1.save()

        portfolio1.artisticGender.add(artisticGender1)
        portfolio1.save()

        artista = Artist()
        artista.photo = "https://conectandomeconlau.com.co/wp-content/uploads/2018/03/%C2%BFTienes-las-caracteri%CC%81sticas-para-ser-un-Artista.png"
        artista.id ="56"
        artista.iban = "AD1400080001001234567890"
        artista.phone = "999999999"
        artista.paypalAccount = "user=artist,password=artist"
        artista.user_id = "43"
        artista.portfolio = portfolio1
        artista.save()

        user2 = User()
        user2.email = "juanjo@juanjo.com"
        user2.username = "artist2"
        user2.password = "artist2"
        user2.id = "44"
        user2.save()

        paymentPackage2 = PaymentPackage()
        paymentPackage2.id = "88"
        paymentPackage2.description = "paymentPackage description 2222222222"
        paymentPackage2.appliedVAT = "0.07"
        paymentPackage2.save()

        portfolio2 = Portfolio()
        portfolio2.id = "3"
        portfolio2.artisticName = "María se fue a la cama a las diez"
        portfolio2.paymentPackage = paymentPackage2
        portfolio2.save()

        artista2 = Artist()
        artista2.photo = "https://conectandomeconlau.com.co/wp-content/uploads/2018/03/%C2%BFTienes-las-caracteri%CC%81sticas-para-ser-un-Artista.png"
        artista2.id = "57"
        artista2.iban = "AD1400080001001234567890"
        artista2.phone = "999999999"
        artista2.paypalAccount = "user=artist,password=artist"
        artista2.user_id = "44"
        artista2.portfolio = portfolio2
        artista2.save()

        response = self.client.get('/artists/?artisticGender=Rock', format='json')
        item_dict = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(item_dict['results']) == 1)
        print(response)

    def test_list_artists_filter_artistic_gender_no_matches(self):

        artisticGender1 = ArtisticGender()
        artisticGender1.name = "Rock"
        artisticGender1.parentGender = None
        artisticGender1.id = "3"
        artisticGender1.save()

        user2 = User()
        user2.email = "juanjo@juanjo.com"
        user2.username = "artist2"
        user2.password = "artist2"
        user2.id = "44"
        user2.save()

        paymentPackage2 = PaymentPackage()
        paymentPackage2.id = "88"
        paymentPackage2.description = "paymentPackage description 2222222222"
        paymentPackage2.appliedVAT = "0.07"
        paymentPackage2.save()

        portfolio2 = Portfolio()
        portfolio2.id = "3"
        portfolio2.artisticName = "María se fue a la cama a las diez"
        portfolio2.paymentPackage = paymentPackage2
        portfolio2.save()

        portfolio2.artisticGender.add(artisticGender1)
        portfolio2.save()

        artista2 = Artist()
        artista2.photo = "https://conectandomeconlau.com.co/wp-content/uploads/2018/03/%C2%BFTienes-las-caracteri%CC%81sticas-para-ser-un-Artista.png"
        artista2.id = "57"
        artista2.iban = "AD1400080001001234567890"
        artista2.phone = "999999999"
        artista2.paypalAccount = "user=artist,password=artist"
        artista2.user_id = "44"
        artista2.portfolio = portfolio2
        artista2.save()

        response = self.client.get('/artists/?artisticGender=Country', format='json')
        item_dict = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(item_dict['results']) == 0)
        print(response)
