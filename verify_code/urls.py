from django.urls import path

from verify_code import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('get_verify/', views.get_verify, name='get_verify'),
    path('login/', views.login, name='login')
]