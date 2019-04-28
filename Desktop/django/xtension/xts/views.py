import os 
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.db import models
from xts.forms import HomeForm


from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.utils.decorators import method_decorator

import json
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

os.environ['DJANGO_SETTINGS_MODULE'] = 'xts.settings'

import django.core.handlers.wsgi
import google.oauth2.credentials
app = django.core.handlers.wsgi.WSGIHandler()
credentials = google.oauth2.credentials.Credentials('3c7a0f589c32d8f873df16ffd9b6910d94e09a5b')
#Always do this at the start of the app

client = language.LanguageServiceClient()

@csrf_exempt
def take_post(request):
	if request.method == "POST":
		#print (request.method)
		#body_unicode = request.body.decode('utf-8').replace('\0', '')
		body_unicode = request.POST.get('text', '')
		document = types.Document(content=body_unicode, 
									type=enums.Document.Type.PLAIN_TEXT)
		sentiment = client.analyze_sentiment(document=document).document_sentiment
		return HttpResponse(sentiment)
	else:
		return HttpResponse("")
	



class classicView(TemplateView):

#BASIC HTML AND CSS DESIGN FOR OUR EXTENSION#
	def get(self, request):
		form = HomeForm()
		#print (sentiment)
		return render(request, 'xts/home.html', {'form': form})

	def features(self, request):
	    return render(request, 'xts/features.html', {'title': 'Features'})

	# #@ensure_csrf_cookie
	# def post(self, request):
	
	# 	form = HomeForm(request.POST)
	# 	if form.is_valid():
	# 		text = form.cleaned_data['post']
	# 		document = types.Document(content=text, 
	# 								type=enums.Document.Type.PLAIN_TEXT)
	# 		sentiment = client.analyze_sentiment(document=document).document_sentiment

	# 	args = {'form': form, 'text': u'Text: {}'.format(sentiment)}
	# 	return render(request, 'xts/post.html', args)
