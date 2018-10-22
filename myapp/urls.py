from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    # ex: /myapp/
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('advertise/', views.advertise, name='advertise'),
    path('signin/', views.signin, name='signin'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('detail/', views.detail, name='detail'),
]