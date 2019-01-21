from django.http import HttpResponse
from django.template import loader


def index(request):
	template = loader.get_template('viewer/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def hottest(request):
	template = loader.get_template('viewer/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def coldest(request):
	template = loader.get_template('viewer/index.html')
	context = {}
	return HttpResponse(template.render(context, request))