# Python Currency Converter

Develop a Python program that will perform currency conversion using data fetched from an open-source API: https://www.frankfurter.app/

Display the current conversion rate between 2 currency codes. It will also calculate the inverse conversion rate between the given 2 currencies. To do so, you will need to call 2 different API endpoints from the Frankfurter app:

Extracting the list of available currency codes https://www.frankfurter.app/docs/#currencies
Extracting the current conversion rate for the specified currency codes https://www.frankfurter.app/docs/#latest 

Command for running the script:
python main.py GBP AUD

The script should return one of the following outputs:
Today's (Date) conversion rate from GBP to AUD is #####. The inverse rate is ####
[ERROR] You haven't provided 2 currency codes
AAA is not a valid option
There is an error with API call

The Currency converter consist of the following files:
main.py : main program used for entering the input parameters (currency codes) and display the results
api.py : python script that will contain the code for calling API endpoints
currency.py : python script that will contain the code for checking if currency code is valid, store results and format final output
test_api.py : python script for testing code from api.py
test_currency.py : python script for testing code from currency.py

![image](https://github.com/gerardo5797/PythonCurrencyConverter/assets/88528474/44e9219f-5ee1-44af-871b-f7e659daaffa)



