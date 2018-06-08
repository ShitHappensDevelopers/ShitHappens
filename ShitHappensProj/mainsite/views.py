from django.shortcuts import render
from . import forms
from .models import Story
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from datetime import datetime, timedelta, timezone
from django.contrib.auth import authenticate, login, logout
from random import randint


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
	loginform = forms.LoginForm()
	return shithappenswithform(request, loginform)

def shithappenswithform(request, loginform):
	stories = Story.objects.all().order_by('like_count').reverse()

	filters_form = None
	if request.method == "POST":
		filters_form = forms.FiltersForm(request.POST)

		if filters_form.is_valid():
			sort_by = filters_form.cleaned_data["sort_by"]
			expire_time = filters_form.cleaned_data["expire_time"]
			last_time = filters_form.cleaned_data["last_time"]
			user_login = filters_form.cleaned_data["user_login"]

			stories = Story.objects.all().order_by(sort_by).reverse()

			# if sort_by == 'like_count':
			# 	stories = stories.reverse()

			if expire_time != 0 and expire_time != None:
				exp_date = datetime.now()+timedelta(hours=expire_time)
				stories = stories.exclude(expire_date=None).exclude(expire_date__gt=exp_date)

			if last_time != 0 and last_time != None:
				cr_date = datetime.now(tz=timezone.utc)-timedelta(hours=last_time) # ??? timezone ??? 
				stories = stories.exclude(create_date__lte=cr_date)

			if user_login != "":
				user = User.objects.get(username=user_login)
				stories = stories.filter(user_id_id=user.id)
	else:
		filters_form = forms.FiltersForm(initial={'sort_by':'like_count'})

	return render(request, "ShitHappens.html", context={ "stories": stories, "loginform":loginform, "filters_form": filters_form })


@login_required
def mystatistic(request):
	return render(request, "MyStat.html")


def main(request):
	return render(request, "Main.html")


@login_required
def mystories(request):
	form_create_story = None
	if (request.method == "POST"):
		form_create_story = forms.CreateNewStory(request.POST)

		if (form_create_story.is_valid()):
			content = form_create_story.cleaned_data["story_content"]
			days_num = form_create_story.cleaned_data["days_num"]
			hours_num = form_create_story.cleaned_data["hours_num"]
			minutes_num = form_create_story.cleaned_data["minutes_num"]

			exp_date = None
			if (days_num != 0 and hours_num != 0 and minutes_num != 0):
				exp_date = datetime.now()+timedelta(days=days_num, hours=hours_num, minutes=minutes_num)

			story_obj = Story(user_id_id=request.user.id, story_content=content, create_date=datetime.now(), 
				expire_date=exp_date, like_count=0, dislike_count=0, is_active=1)

			story_obj.save()
	else:
		form_create_story = forms.CreateNewStory()

	stories = Story.objects.filter(user_id_id=request.user.id)
	return render(request, "MyStories.html", context={ "stories": stories, "form_create_story": form_create_story} )


def loginview(request):
	loginform = forms.LoginForm(request.POST)
	if loginform.is_valid():
		username = loginform.cleaned_data['username']
		passwd = loginform.cleaned_data['passwd']
		user = authenticate(request, username=username, password=passwd)
		if user is not None:
			login(request, user)
		else:
			loginform.add_error("__all__", "Неправильный логин, имейл или пароль")
			return shithappenswithform(request, loginform)
	return  redirect('home-page')


def logoutview(request):
	logout(request)
	return  redirect('home-page')

def registernewuserview(request):
	registernewuserform = None
	if request.method == 'POST':
		registernewuserform = forms.RegisterNewUserForm(request.POST)
		if registernewuserform.is_valid():
			username = registernewuserform.cleaned_data['username']
			email = registernewuserform.cleaned_data['email']
			passwd = registernewuserform.cleaned_data['passwd1']
			user = User.objects.create_user(username, email, passwd)
			print(username)
			return  redirect('home-page')
	else:
		registernewuserform = forms.RegisterNewUserForm()
	return render(request, "forms.html", context={ "registernewuserform": registernewuserform})


def singlestory(request,storyid):
	story = Story.objects.get(pk=storyid)
	if not story == None:
		redirect('home-page')
	return render(request, "singlestory.html", context={ "story": story})

def randomstory(request):
	numberofstories = Story.objects.all().count()
	storynum = randint(0,numberofstories-1)
	story = Story.objects.all().order_by("pk")[storynum]
	return redirect(story.get_absolute_url())
