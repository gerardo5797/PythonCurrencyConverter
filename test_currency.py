import unittest
from currency import check_valid_currency, extract_api_result, Currency


class TestValidCurrency(unittest.TestCase):

    def test_valid_currency(self):
        result = check_valid_currency("USD")
        self.assertEqual(result, True)

    def test_invalid_currency(self):
        result = check_valid_currency("ABC")
        self.assertEqual(result, False)


class TestClassEAPI(unittest.TestCase):
    def test_class_eapi(self):
        from_currency = "USD"
        to_currency = "GBP"
        amount = 1
        rate = 0.72282
        date = "2021-09-16"
        currency_class = Currency(from_currency, to_currency, amount, rate, float, date)

        self.assertEqual(currency_class.from_currency, from_currency)
        self.assertEqual(currency_class.to_currency, to_currency)
        self.assertEqual(currency_class.amount, amount)
        self.assertEqual(currency_class.rate, rate)
        self.assertEqual(currency_class.date, date)
        self.assertEqual(currency_class.from_currency, from_currency)
