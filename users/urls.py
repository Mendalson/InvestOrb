from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # path('', views, name='index'),
    path('login/', views.login_view, name='login'),
]
