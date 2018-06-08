from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls import include


urlpatterns = [
	path('someurl', RedirectView.as_view(url='/')),
	path('myprofile/<acttype>', views.myprofile, name='myprofilepattern-action'),
	path('myprofile', views.myprofile, name='myprofilepattern' ),
	#path('base', views.about),
	path('AboutUs', views.about, name='aboutusurl'),
	path('Stat', views.statistic, name='staturl'),
	path('ShitHappens', views.shithappens, name='home-page'),
	path('MyStat', views.mystatistic),
	path('Main', views.main),
	path('MyStories', views.mystories, name='createStory'),
	path('login', views.loginview, name='loginurl'),
	path('logout', views.logoutview, name='logouturl'),
	path('register', views.registernewuserview, name='registernewuserurl'),
	path('singlestory/<int:storyid>', views.singlestory, name='singlestoryurl'),
	path('randomstory', views.randomstory, name='randomstoryurl'),
]
