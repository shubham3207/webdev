from Owner.views import index, Profile

from django.urls import reverse,resolve

from django.test import SimpleTestCase

from django.test.client import Client

from .views import *



class TestUrls(SimpleTestCase):

    def test_index_url(self):

        url=reverse("Owner")

        self.assertEquals(resolve(url).func,index)

    

    

  