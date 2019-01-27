from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from . import services


def index(request):
	template = loader.get_template('viewer/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def get_btc_price(request):
	print("request received")
	# TODO get lat,lng from request
	country_code = services.get_country_from_coordinates(1.0, 1.0)
	currency_code = services.get_country_currency(country_code)
	btc_price = services.get_btc_price(currency_code)
	return JsonResponse({'btc_price': btc_price})