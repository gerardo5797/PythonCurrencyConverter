import sys
from api import call_api, format_latest_url
from currency import check_valid_currency, extract_api_result


def main():
    """
    Function that will check if there are enough input arguments provided.
    If so it will return the formatted result from the Frankfurter app.
    If not it will return an error message

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    if the number of arguments, excluding the first is exactly 2
        Execute the function 'get rates' with the input arguments
    if the number of arguments excluding the first is less than 2
        Display an error message indicating not enough arguments have been provided
    if the number of arguments excluding the first is greater than 2
        Display an error message indicating more arguments than needed have been provided

    Returns
    -------
    str
        Formatted API result or error message
    """
    if len(sys.argv[1:]) == 2:
        get_rate(sys.argv[1], sys.argv[2])
    elif len(sys.argv[1:]) < 2:
        return print("[ERROR] You haven't provided 2 currency codes")
    elif len(sys.argv[1:]) > 2:
        return print("[ERROR] You have provided more than 2 currency codes")




def get_rate(from_currency: str, to_currency: str):
    """
    Function that will check if provided currency codes are valid otherwise it will return error message.
    If both are valid, it will format the API url, make a request to it and format the result

    Parameters
    ----------
    from_currency : str
        Currency code to be converted from
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    Check if the first argument/'from currency' is a valid currency
    Check if the second argument/'to currency' is a valid currency

    if both are True
        make a Get request to the latest endpoint for the valid currencies
        extract the relevant fields from the resulting dictionary from the method json of response
        display the success message

    if only the first argument/'from currency' is a valid currency code
        display message indicating the second argument/'to currency' is not valid

    if only the second argument/'to currency' is a valid currency code
        display message indicating the first argument/'from currency' is not valid

    otherwise
        display message indicating the both arguments/'from currency' - 'to currency' are not valid


    Returns
    -------
    str
        Formatted API result or error message
    """

    from_check = check_valid_currency(from_currency)
    to_check = check_valid_currency(to_currency)

    if from_check and to_check:
        _CLASS_ = extract_api_result(call_api(format_latest_url(from_currency, to_currency)).json())
        return _CLASS_.format_result()
    elif from_check:
        return print( to_currency + " " + "is not a valid option")
    elif to_check:
        return print( from_currency + " " "is not a valid option")
    else:
        return print("Both" + " " + from_currency + " " + "and" + " " + to_currency + " " + "are invalid options")


if __name__ == "__main__":
    main()
