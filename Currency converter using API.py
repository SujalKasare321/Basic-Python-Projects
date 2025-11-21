
import requests

def currency_converter(amount,from_currency,to_currency):

    url=f"https://open.er-api.com/v6/latest/{from_currency}"
    response=requests.get(url)
    data=response.json()
    
    if data.get("result")=="success":
        rates=data["rates"]
        converted_amount=amount*rates[to_currency]
        print(f"{amount} {from_currency} : {converted_amount} {to_currency} " )
    else:
        print("ERROR! Couldnt fetch exchange rates")
        
amount=float(input("Enter amount:"))
from_currency=input("From Currency(INR/USD/EUR):").upper()
to_currency=input("To Currency(USD/INR/EUR):").upper()

currency_converter(amount,from_currency,to_currency)

