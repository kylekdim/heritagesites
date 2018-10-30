#Lines 1-6 Commented Out for HW #6
#from django.shortcuts import render
#from django.http import HttpResponse


#def index(request):
#   return HttpResponse("Hello, world. You're at the UNESCO Heritage Sites index.")

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import HeritageSite


def index(request):
	return HttpResponse("Hello, world. You're at the UNESCO Heritage Sites index page.")


class AboutPageView(generic.TemplateView):
	template_name = 'heritagesites/about.html'


class HomePageView(generic.TemplateView):
	template_name = 'heritagesites/home.html'


class SiteListView(generic.ListView):
	model = HeritageSite
	context_object_name = 'sites'
	template_name = 'heritagesites/site.html'
	paginate_by = 50

	def get_queryset(self):
		return HeritageSite.objects.all().order_by('site_name')# TODO write ORM code to retrieve all Heritage Sites
#.select_related('heritage_site_category') originally between two ORM statements above

class SiteDetailView(generic.DetailView):
	model = HeritageSite
	context_object_name = 'site'
	template_name = 'heritagesites/site_detail.html'
	# TODO add the correct template string value

class CountryAreaListView(generic.ListView):
	model = CountryArea
	context_object_name = 'countries'
	template_name = 'heritagesites/country_area.html'
	paginate_by = 20

	def get_queryset(self):
		return CountryArea.objects.select_related('location').select_related('dev_status').order_by('country_area_name')

class CountryAreaDetailView(generic.DetailView):
	model = CountryArea
	template_name = 'heritagesites/country_area_detail.html'