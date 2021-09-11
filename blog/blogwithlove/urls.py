from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('years/',views.years,name='years'),
    path('viewgdp/',views.viewgdp,name='viewgdp'),
    path('search',views.search,name='search'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

]
