from django.urls import path
from . import views


app_name = 'accrualapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
]
