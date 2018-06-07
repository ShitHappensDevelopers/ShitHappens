from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls import include


urlpatterns = [
	path('someurl', RedirectView.as_view(url='/')),
	path('myprofile/<acttype>', views.myprofile, name='myprofilepattern-action'),
	path('myprofile', views.myprofile, name='myprofilepattern' ),
	#path('base', views.about),
	path('AboutUs', views.about),
	path('Stat', views.statistic),
	path('ShitHappens', views.shithappens, name='home-page'),
	path('MyStat', views.mystatistic),
	path('Main', views.main),
	path('MyStories', views.mystories),
	path('login', views.loginview, name='loginurl'),
	path('logout', views.logoutview, name='logouturl'),
]
