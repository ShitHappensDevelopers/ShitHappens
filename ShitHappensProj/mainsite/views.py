from django.shortcuts import render
from . import forms
from .models import Story
from django.contrib.auth.decorators import login_required

# Create your views here.

def about(request):
	return render(request, "AboutUs.html")



def myprofile(request, acttype=None):
	if acttype != None and request.method == 'POST':
		pass

	else:
		formchangeEmail = forms.MyProfileChangeEmailForm()
		formchangeUsername = forms.MyProfileChangeUsernameForm()
		formchangePasswd = forms.MyProfileChangePasswdForm()

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
