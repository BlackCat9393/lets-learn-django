from django.views.generic.base import View, TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, datetime


class AnotherHelloWorldView(TemplateView):
	template_name = 'helloWorld.html'
	def get_context_data(self):
		return {'date':date.today(), 'time':datetime.now()}

class NewHelloWorldView(View):
	def get(self, request):
		return render(request, 'helloWorld.html',
			{'date':date.today(), 'time':datetime.now()})

class HelloWorldView(View):
	def get(self, request):
		return HttpResponse('\thello world :D')

class TestView(View):
	def get(self, request):
		return HttpResponse(f'{request}')