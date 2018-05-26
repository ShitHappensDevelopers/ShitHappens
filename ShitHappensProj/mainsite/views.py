from django.shortcuts import render
from . import forms

# Create your views here.

def about(request):
	return render(request, "base.html")



def myprofile(request, acttype=None):
	if acttype != None and request.method == 'POST':
		pass

	else:
		formchangeEmail = forms.MyProfileChangeEmailForm()
		formchangeUsername = forms.MyProfileChangeUsernameForm()
		formchangePasswd = forms.MyProfileChangePasswdForm()

	return render(request, 'myprofile.html', context={'formchangeEmail': formchangeEmail, 'formchangeUsername':formchangeUsername, 'formchangePasswd': formchangePasswd }
	 )