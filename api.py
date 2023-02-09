import requests

_HOST_ = 'https://api.frankfurter.app'
_CURRENCIES_ = '/currencies'
_LATEST_ = '/latest'


def call_api(url: str) -> None:
    """
    Function that will call the specified API endpoint and return the response

    Parameters
    ----------
    url : str
        URL of the API endpoint to be called

    Pseudo-code
    ----------
    Make a Get request from a URL and save it into a variable response
    if the response status code is 200
        return response
    otherwise
        display API error message

    Returns
    -------
    requests.models.Response
        Response from API request
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        return print("There is an error with API call")


def format_currencies_url() -> str:
    """
    Function that will format the URL to the currency endpoint

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    Concatenate right parts of the URL and save it into a variable.

    Returns
    -------
    str
        Formatted URL to the currency endpoint
    """
    currencies_url = _HOST_ + _CURRENCIES_
    return currencies_url


def get_currencies():
    """
    Function that will extract the currency codes available from the Frankfurter app as a list

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    Make get request to the currency endpoint
    Store the method json of response into a variable in the form of a dictionary
    Extract the keys from the dictionary and store them as a list in a new variable

    Returns
    -------
    list
        Currency codes available from the Frankfurter app
    """

    response_currencies = call_api(format_currencies_url())
    dict_currency = response_currencies.json()
    list_currency = list(dict_currency.keys())
    return list_currency


def format_latest_url(from_currency: str, to_currency: str) -> str:
    """
    Function that will format the URL to the latest endpoint

    Parameters
    ----------
    from_currency : str
        Currency code to be converted from
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    Concatenate right parts of the URL and save it into a variable.

    Returns
    -------
    str
        Formatted URL to the latest endpoint
    """
    latest_url = _HOST_ + _LATEST_ + '?from=' + from_currency + '&to=' + to_currency
    return latest_url
