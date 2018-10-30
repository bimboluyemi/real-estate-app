from django.urls import path

from myapp.views import pages

app_name = 'myapp'
urlpatterns = [
    path('', pages.home, name='home'),
    path('search/', pages.search, name='search'),
    path('advertise/', pages.advertise, name='advertise'),
    path('signin/', pages.signin, name='signin'),
    path('contact/', pages.contact, name='contact'),
    path('about/', pages.about, name='about'),
    path('detail/', pages.detail, name='detail'),
]
