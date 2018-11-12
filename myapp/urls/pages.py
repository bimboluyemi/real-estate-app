from django.urls import path
from myapp.views import pages
from myapp.views.account import LoginView, LogoutView, DashboardView

app_name = 'myapp'
urlpatterns = [
    path('', pages.HomePageView.as_view(extra_context={'title': 'Home'}), name='home'),
    path('contact/', pages.ContactPageView.as_view(extra_context={'title': 'Contact Us'}), name='contact'),
    path('about/', pages.AboutPageView.as_view(extra_context={'title': 'About Us'}), name='about'),
    path('detail/', pages.DetailPageView.as_view(), name='detail'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]
