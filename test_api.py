import unittest
from api import call_api, format_currencies_url, get_currencies, format_latest_url, _HOST_, _LATEST_, _CURRENCIES_


class TestFormatUrl(unittest.TestCase):
    def test_format_currencies_url(self):
        result = format_currencies_url()
        self.assertEqual(result, "https://api.frankfurter.app/currencies")


    def test_format_currencies_url2(self):
        result = format_currencies_url()
        self.assertEqual(result, _HOST_ + _CURRENCIES_)


    def test_format_latest_url(self):
        result = format_latest_url("GBP", "AUD")
        self.assertEqual(result, "https://api.frankfurter.app/latest?from=GBP&to=AUD")


    def test_format_latest_url2(self):
        result = format_latest_url("GBP", "AUD")
        self.assertEqual(result, _HOST_ + _LATEST_ + '?from=' + "GBP" + "&to=" + "AUD")


class TestAPI(unittest.TestCase):
    def test_api_currencies_status_code(self):
        result = call_api(format_currencies_url()).status_code
        self.assertEqual(result, 200)


    def test_api_latest_status_code(self):
        result = call_api(format_latest_url("GBP", "AUD")).status_code
        self.assertEqual(result, 200)


class TestGetCurrenciesType(unittest.TestCase):
    def test_name(self):
        result = type(get_currencies())
        self.assertEqual(result, list)