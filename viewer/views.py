from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseServerError
from django.template import loader

import json
from django.views.decorators.csrf import csrf_exempt
from . import services
from . import exceptions as e


def index(request):
	template = loader.get_template('viewer/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

@csrf_exempt
def get_btc_price(request):
	try:
		# parse {lat,lng} from request
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		lat = float(body['lat'])
		lng = float(body['lng'])
		# get btc price info from {lat,lng}
		result = services.get_location_btc_price_info(lat, lng)
		return JsonResponse(result)

	except e.LocationBtcPriceException as ex:
		result = {'failure_message': str(ex)}
		return JsonResponse(result)


