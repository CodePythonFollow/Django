from django.urls import path

from three import views

urlpatterns = [
    path('home/', views.home, name='home')
]