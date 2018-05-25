from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
	path('someurl', RedirectView.as_view(url='/')),
	#path('base', views.about),
	path('AboutUs', views.about),
	path('Stat', views.statistic),
	path('ShitHappens', views.shithappens),
	path('MyStat', views.mystatistic),
]