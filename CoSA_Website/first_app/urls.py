from django.urls import path, include
from . import views
from django.contrib.auth.views import logout

app_name = 'first_app'

urlpatterns =  [
                    path('', views.index, name='home'),
                    path('knowYourCouncil/', views.knowYC, name='knowYC'),
                    path('register/', views.register, name='Register'),
                    path('login/', views.loginView, name='Login'),
                    path('logout/', logout, {'next_page':'/'}, name='Logout')
                ]   