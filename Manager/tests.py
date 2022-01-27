from Manager.views import index, Profile

from django.urls import reverse,resolve

from django.test import SimpleTestCase

from django.test.client import Client

from .views import *



class TestUrls(SimpleTestCase):

    def test_index_url(self):

        url=reverse("Manager")

        self.assertEquals(resolve(url).func,index)

    

    def test_profile_url(self):

        url=reverse("Profile")

        self.assertEquals(resolve(url).func,Profile)

    def test_AllCustomers_url(self):

        url=reverse("AllCustomers")

        self.assertEquals(resolve(url).func,AllCustomers)
    def test_AllVehicles_url(self):

        url=reverse("AllVehicles")

        self.assertEquals(resolve(url).func,AllVehicles)
    def test_RentRequest_url(self):

        url=reverse("RentRequest")

        self.assertEquals(resolve(url).func,RentRequest)