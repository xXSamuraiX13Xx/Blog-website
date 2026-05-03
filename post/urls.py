from django.urls import path
from .views import *


urlpatterns = [
	
	path('<slug:slug>',  postID),
	path('index/<slug:slug>', postID),
	path("", indexec),
	path("index/", indexec),
	path('category/', category),
	path("index/category/", category),
	path("Technology/", technology),
	path("index/Technology/", technology),
	path("General/", general),
	path("index/General/", general),
	path("Health&Fitness/", health_fitness),
	path("index/Health&Fitness/", health_fitness),
	path("Unsolved/", unsolved),
	path("index/Unsolved/", unsolved),
	path("Self-improvement/", self_improvement),
	path("index/Self-improvement/", self_improvement),
	path('contact/', contact),
	path("index/contact/", contact),
	path('PrivacyPolicy/', PrivacyPolicy),
	path("index/PrivacyPolicy/", PrivacyPolicy),
	]
