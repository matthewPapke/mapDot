from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt
from . import services


def index(request):
	template = loader.get_template('viewer/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

@csrf_exempt
def get_btc_price(request):
	# parse {lat,lng} from request
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	lat = float(body['lat'])
	lng = float(body['lng'])
	# get country from {lat,lng}
	country = services.get_country_from_coordinates(lat, lng)
	country_code = country['country_code']
	# get currency and BTC price conversion for given country
	currency = services.get_country_currency(country_code)
	btc_price = services.get_btc_price(currency['alpha3'])
	return JsonResponse({'btc_price': btc_price, 'currency_name': currency['name'], 'country_name': country['country_name']})