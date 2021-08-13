from django.test import TestCase
import unittest
import datetime
from .models import Order


class TestOrder(TestCase):
   
    def test_successful_order(self):
        data= {
            'isin':'wednesdayweu',
            'limit_price': 2,
            'side':'buy',
            'valid_until':int(datetime.datetime.now().timestamp()),
            'quantity':4

        }
        res=self.client.post("/api/order/",  format="json", data=data)      
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data['isin'], data['isin'])
        self.assertEqual(res.data['side'], data['side'])
        self.assertEqual(res.data['limit_price'], data['limit_price'])
        self.assertEqual(res.data['valid_until'], data['valid_until'])
        self.assertEqual(res.data['quantity'], data['quantity'])


    def test_negative_quantity(self):
        data= {
            'isin':'wednesdayweu',
            'limit_price': 2,
            'side':'buy',
            'valid_until':int(datetime.datetime.now().timestamp()),
            'quantity':-4

        }
        res=self.client.post("/api/order/",  format="json", data=data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(res.data.get('quantity'))
        

    def test_side_case_tolerance(self):
        data= {
            'isin':'wednesdayweu',
            'limit_price': 2,
            'side':'BUY',
            'valid_until':int(datetime.datetime.now().timestamp()),
            'quantity':4

        }
        res=self.client.post("/api/order/",  format="json", data=data)
        self.assertEqual(res.status_code, 201)


    def test_reduce_isin_length(self):
        data= {
            'isin':'wednesdaywe',
            'limit_price': 2,
            'side':'BUY',
            'valid_until':int(datetime.datetime.now().timestamp()),
            'quantity':4

        }
        res=self.client.post("/api/order/",  format="json", data=data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(res.data.get('isin'))


    def test_negative_limit_price(self):
        data= {
            'isin':'wednesdaywed',
            'limit_price': -2,
            'side':'BUY',
            'valid_until':int(datetime.datetime.now().timestamp()),
            'quantity':4

        }
        res=self.client.post("/api/order/",  format="json", data=data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(res.data.get('limit_price'))


    def test_valid_umtil(self):
        data= {
            'isin':'wednesdaywed',
            'limit_price': 2,
            'side':'BUY',
            'valid_until': -5,
            'quantity':4
        }
        res=self.client.post("/api/order/",  format="json", data=data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(res.data.get('valid_until'))
