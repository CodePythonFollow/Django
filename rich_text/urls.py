from django.urls import path

from rich_text import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('edit/', views.edit, name='edit')
]