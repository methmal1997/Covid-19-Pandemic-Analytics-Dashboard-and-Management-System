from django.urls import path
from .import views
from .views import HomeView, AddPost, UpdatePost, DeletePost

urlpatterns = [
    path('index2', views.index2, name='index2'),
    path('news', views.news, name='news'),
    path('lnews', views.lnews, name='lnews'),
    path('guide', views.guide, name='guide'),
    path('', views.dashboard, name='dashboard'),
    path('covidtest', views.covidtest, name='covidtest'),
    path('hospital', views.hospital, name='hospital'),
    path('vaccination', views.vaccination, name='vaccination'),
    path('fund', HomeView.as_view(), name='fund'),
    path('add_post', AddPost.as_view(), name='add_post'),
    path('update_post/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('<int:pk>/remove', DeletePost.as_view(), name='delete_post'),
    path('world', views.world, name='world'),
    path('test', views.test, name='test'),
    path('temp', views.temp, name='temp'),
    path('info', views.info, name='info'),
    path('sl', views.sl, name='sl'),
]
