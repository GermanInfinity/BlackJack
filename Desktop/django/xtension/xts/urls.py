from django.urls import path 
from django.conf.urls import url 
from . import views
from xts.views import classicView
urlpatterns = [
    #first arguement is pattern to match       #views. is py file. home is the method(function)
	#path('', views.home, name='Extension-home'),
    #path('features', views.features, name='Features-page'),
    path('post', views.take_post, name='Posts for storing'),
    #url(r'post', classicView.as_view(), name='post request'),
    url(r'', classicView.as_view(), name='home')
]
