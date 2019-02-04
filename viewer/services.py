import reverse_geocoder as rg
import pycountry as pyc
from forex_python.bitcoin import BtcConverter
from babel import numbers

# reverse geocode {lat,lng}
def get_country_from_coordinates(lat, lng):
	coordinates = (lat,lng)
	country_results = rg.search(coordinates)
	country = country_results[0]
	country_code = country.get('cc')
	country_name = pyc.countries.get(alpha_2=country_code).name
	return {'country_name': country_name, 'country_code': country_code}

# get currency from country code
def get_country_currency(country_code):
	country = pyc.countries.get(alpha_2=country_code)
	currency = pyc.currencies.get(numeric=country.numeric)
	return {'alpha3': currency.alpha_3, 'name': currency.name}

# convert currency to BTC
def get_btc_price(currency_code):
	b = BtcConverter() 
	price = b.get_latest_price(currency_code)
	formatted_price = numbers.format_currency(price, currency_code, locale='en')
	return formatted_price
