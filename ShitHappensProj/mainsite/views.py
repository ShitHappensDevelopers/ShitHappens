from django.shortcuts import render
from .models import Story

# Create your views here.

def about(request):
	return render(request, "AboutUs.html")


def statistic(request):
	all_stories_num = Story.objects.all().count()
	available_stories_num = Story.objects.filter(is_active=True).count()
	disappear_stories_num = 1;

	data = { "all_stories_num": all_stories_num, 
	"available_stories_num": available_stories_num,
	"disappear_stories_num": disappear_stories_num };

	return render(request, "Stat.html", context=data)


def shithappens(request):
	stories = Story.objects.all()
	data = { "stories": stories }
	return render(request, "ShitHappens.html", context=data)


def mystatistic(request):
	return render(request, "MyStat.html")
