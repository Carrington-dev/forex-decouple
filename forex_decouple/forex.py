from decimal import Decimal
import requests

def exchange_currency(from_currency, to_currency, amount):
    response = requests.get(f"https://api.frankfurter.app/latest?amout={amount}&from={from_currency}&to={to_currency}")
    if response.ok:
        rate =  round( response.json()['rates'][to_currency], 2)
        return float(round( Decimal(amount) / Decimal(rate), 2))
    return "An error has occured make sure you have internet connection"

def get_all_currencies():
    response = requests.get(f"https://api.frankfurter.app/latest")
    if response.ok:
        rates = response.json()
        return rates
    return "An error has occured make sure you have internet connection"
    