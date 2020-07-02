from django.urls import path

from paginator_app import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('getdata/', views.getdata, name='getdata')
]