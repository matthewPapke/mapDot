import reverse_geocoder as rg
import pycountry as pyc
from forex_python.bitcoin import BtcConverter
from babel import numbers
from . import exceptions as e


def get_location_btc_price_info(lat, lng):
	country = get_country_from_coordinates(lat,lng)
	if country is None:
		raise e.LocationBtcPriceException('Unable to reverse geocode coordinates')
		# return {'failure_message': 'Unable to reverse geocode coordinates'}
	
	currency = pyc.currencies.get(numeric=country.numeric)
	if currency is None:
		raise e.LocationBtcPriceException('Unable to get currency information about {}'.format(country.name))
		# return {'failure_message': 'Unable to get currency information about country'}
	
	# get currency and BTC price conversion for given country
	btc_price = get_btc_price(currency.alpha_3)
	if btc_price is None:
		raise e.LocationBtcPriceException('BTC exchange rate is not available for currency {}'.format(currency.name))
		# return {'failure_message': 'BTC exchange rate is not available for currency'}

	# return location, currency, and btc information
	return {'btc_price': btc_price, 'currency_name': currency.name, 'country_name': country.name}


# reverse geocode {lat,lng}
def get_country_from_coordinates(lat, lng):
	country_results = rg.search((lat,lng))
	country = country_results[0]
	country_code = country.get('cc')
	return pyc.countries.get(alpha_2=country_code)

	
# convert currency to BTC
def get_btc_price(currency_code):
	b = BtcConverter() 
	price = b.get_latest_price(currency_code)
	if price is not None:
		return numbers.format_currency(price, currency_code, locale='en')
	else:
		return None
