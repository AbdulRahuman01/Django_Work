from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # homepage
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('counter/', views.counter_view, name='counter'),
]
