from dataclasses import dataclass
from api import get_currencies

CURRENCIES = get_currencies()


def check_valid_currency(currency: str) -> bool:
    """
    Function that will check currency code is amongst the list of available currencies

    Parameters
    ----------
    currency : str
        Currency code to be checked

    Pseudo-code
    ----------
    If item/currency is in the Variable CURRENCIES (List of currency codes)
        item/currency is True/valid
    If item/currency is not in the Variable CURRENCIES (List of currency codes)
        item/currency is False / not valid


    Returns
    -------
    bool
        True if the currency code is valid otherwise False
    """

    if currency in CURRENCIES:
        checking = True
    else:
        checking = False
    return checking


@dataclass
class Currency:
    """
    Class that represents a Currency conversion object.

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    """
    from_currency: str = None
    to_currency: str = None
    amount: float = 0
    rate: float = 0
    inverse_rate: float = 0
    date: str = None

    def reverse_rate(self):
        """
        Method that will calculate the inverse rate, round it to 5 decimal places and save it in the attribute inverse_rate

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.inverse_rate = round(1 / self.rate, 5)

    def format_result(self):
        """
        Methods returning the formatted successful message

        Parameters
        ----------
        None

        Returns
        -------
        str
            Formatted successful message
        """
        return print("Today's" + " " + "("+ self.date +")" + " " + "conversion rate from" + " " +
        self.from_currency+ " " + "to" + " " + self.to_currency + " " + "is" + " " + str(self.rate) +
        "." + " "+ "The inverse rate is" + " "+ str(self.inverse_rate))


def extract_api_result(result: dict) -> Currency:
    """
    Function that will extract the relevant fields from API result, instantiate a Currency class accordingly and
    calculate the inverse rate

    Parameters
    ----------
    result : dict
        Results of the API converted as dictionary

    Pseudo-code
    ----------
    Get the 'base' key from the dictionary and store it as the 'from_currency' attribute.
    Get the 'rates' key from the dictionary as a list and then extract the first key from such list and store it as the
    'to_currency' attribute.
    Get the 'amount' key from the dictionary.
    Get the 'rates' key from the dictionary as a list then extract the first value from such list and store it as the
    'rate' attribute.
    Get the 'date' key from the dictionary and store it as the 'date' attribute.
    Instantiate the Currency class containing the attributes
    Calculate the inverse rate using the 'reverse_rate' method from the class 'Currency'

    Returns
    -------
    Currency
        Instantiated Currency
    """
    from_currency = result.get('base')
    to_currency = list(result.get('rates').keys())[0]
    amount = result.get('amount')
    rate = list(result.get('rates').values())[0]
    date = result.get('date')
    currency_class = Currency(from_currency, to_currency, amount, rate, float, date)
    currency_class.reverse_rate()

    return currency_class


