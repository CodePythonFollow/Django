from django.urls import path

from Two import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('get_redis', views.get_redis, name="get_redis"),
]