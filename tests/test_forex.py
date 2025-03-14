import unittest
from forex_decouple.forex import exchange_currency, get_all_currencies

class TestModule1(unittest.TestCase):
    def test_exchange_currency(self):
        self.assertEqual(exchange_currency(from_currency="USD", to_currency="ZAR", amount=890), 48.95)
    
    def test_get_all_currencies(self):
        expected = {"amount":1.0,"base":"EUR","date":"2024-08-01","rates":{"AUD":1.6501,"BGN":1.9558,"BRL":6.112,"CAD":1.4912,"CHF":0.9467,"CNY":7.8203,"CZK":25.454,"DKK":7.4613,"GBP":0.84328,"HKD":8.432,"HUF":395.55,"IDR":17549,"ILS":4.0855,"INR":90.35,"ISK":149.9,"JPY":162.66,"KRW":1474.13,"MXN":19.9936,"MYR":4.9295,"NOK":11.7465,"NZD":1.814,"PHP":62.912,"PLN":4.2958,"RON":4.9756,"SEK":11.522,"SGD":1.4437,"THB":38.409,"TRY":35.706,"USD":1.0789,"ZAR":19.6134}}

        self.assertEqual(get_all_currencies(), expected)

if __name__ == '__main__':
    unittest.main()
