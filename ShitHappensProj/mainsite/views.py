from django.shortcuts import render
from . import forms
from .models import Story
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.

def about(request):
	return render(request, "AboutUs.html")


@login_required
def myprofile(request, acttype=None):
	formchangeEmail = None
	formchangeUsername = None
	formchangePasswd = None
	if acttype != None and request.method == 'POST':
		if acttype == 'changeemail':
			formchangeEmail = forms.MyProfileChangeEmailForm(request.POST)
			if formchangeEmail.is_valid():		
				request.user.email = formchangeEmail.cleaned_data['new_email']
				request.user.save()
				newemail= formchangeEmail.cleaned_data['new_email']
				print("set new email to "+ newemail)
				return redirect('myprofilepattern')
		if acttype == 'changeusername':
			formchangeUsername = forms.MyProfileChangeUsernameForm(request.POST)
			if formchangeUsername.is_valid():		
				request.user.username = formchangeUsername.cleaned_data['new_username']
				request.user.save()
				newusername= formchangeUsername.cleaned_data['new_username']
				print("set new username to " + newusername)
				return redirect('myprofilepattern')
		if acttype == 'changepasswd':
			formchangePasswd = forms.MyProfileChangePasswdForm(request.POST)
			if formchangePasswd.is_valid():	
				oldpassword = formchangePasswd.cleaned_data['old_password']
				newpassword = formchangePasswd.cleaned_data['new_password1']
				if (request.user.check_password(oldpassword)):
					request.user.set_password(newpassword)
					request.user.save()
					print("set new password  to " + newpassword)
					return redirect('myprofilepattern')
				else:
					formchangePasswd.add_error('old_password', 'Неправильный старый пароль')
				

	if not formchangeEmail:
		formchangeEmail = forms.MyProfileChangeEmailForm()
		print("new formchangeEmail")
	if not formchangeUsername:
		formchangeUsername = forms.MyProfileChangeUsernameForm()
		print("new formchangeUsername")
	if not formchangePasswd:
		formchangePasswd = forms.MyProfileChangePasswdForm()
		print("new formchangePasswd")

	return render(request, 'myprofile.html', context={'formchangeEmail': formchangeEmail, 'formchangeUsername':formchangeUsername, 'formchangePasswd': formchangePasswd })


def statistic(request):
	all_stories_num = Story.objects.all().count()
	available_stories_num = Story.objects.filter(is_active=True).count()
	disappear_stories_num = 1;

	data = { "all_stories_num": all_stories_num,
	"available_stories_num": available_stories_num,
	"disappear_stories_num": disappear_stories_num };

	return render(request, "Stat.html", context=data)


def shithappens(request):
	stories = Story.objects.all().order_by('like_count').reverse()
	print(stories)
	return render(request, "ShitHappens.html", context={ "stories": stories })


@login_required
def mystatistic(request):
	return render(request, "MyStat.html")


def main(request):
	return render(request, "Main.html")


@login_required
def mystories(request):
	stories = Story.objects.filter(user_id_id=request.user.id)
	return render(request, "MyStories.html", context={ "stories": stories });
