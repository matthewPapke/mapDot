from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseServerError
from django.http import HttpResponseBadRequest
from django.template import loader
import json
from . import services
from . import exceptions as e


def index(request):
	template = loader.get_template('viewer/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def get_btc_price(request):
	try:
		if request.method != 'GET':
			return HttpResponseNotAllowed('This is a GET-only endpont')

		# parse {lat,lng} from request
		lat = float(request.GET.get('lat', ''))
		lng = float(request.GET.get('lng', ''))

		# get btc price info from {lat,lng}
		result = services.get_location_btc_price_info(lat, lng)
		return JsonResponse(result)

	except ValueError as ex:
		return HttpResponseBadRequest("Invalid lat and lng parameters in request")
		print(str(ex))

	except Exception as ex:
		print(str(ex))
		return HttpResponseServerError()


