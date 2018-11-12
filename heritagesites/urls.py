#from django.urls import path

#from . import views

#urlpatterns = [
   #path('', views.index, name='index'),
#]

#Above commented out for HW6

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    #The two URLs below were added during the midterm:
    path('countries/', views.CountryAreaListView.as_view(), name='countries'),
    path('countries/<int:pk>/', views.CountryAreaDetailView.as_view(), name='country_detail'),
    #end midterm entry
    path('sites/', views.SiteListView.as_view(), name='sites'),
    path('sites/<int:pk>/', views.SiteDetailView.as_view(), name='site_detail'),

    #entries below added as a part of HW8
    path('sites/new/', views.SiteCreateView.as_view(), name='site_new'),
    path('sites/<int:pk>/delete/', views.SiteDeleteView.as_view(), name='site_delete'),
	path('sites/<int:pk>/update/', views.SiteUpdateView.as_view(), name='site_update'),
]