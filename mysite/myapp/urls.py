from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path('news', views.news, name='news'),
    path('lnews', views.lnews, name='lnews'),
    path('guide', views.guide, name='guide'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('covidtest', views.covidtest, name='covidtest'),
    path('hospital', views.hospital, name='hospital'),
    path('vaccination', views.vaccination, name='vaccination'),
    path('fund', views.fund, name='fund'),
    path('world', views.world, name='world'),
    path('test', views.test, name='test'),
    path('temp', views.temp, name='temp'),
    path('info', views.info, name='info'),
]
