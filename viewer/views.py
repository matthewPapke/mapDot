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

# given {lat,lng}, return the country and the price of Bitcoin
@csrf_exempt
def get_btc_price(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	country = services.get_country_from_coordinates(float(body['lat']), lng = float(body['lng']))
	country_code = country['country_code']
	currency_code = services.get_country_currency(country_code)
	btc_price = services.get_btc_price(currency_code)
	return JsonResponse({'btc_price': btc_price, 'country_name': country['country_name']})