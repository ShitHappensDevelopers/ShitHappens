from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
path('someurl', RedirectView.as_view(url='/')),
]