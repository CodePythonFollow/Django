from django.urls import path

from app import views

urlpatterns = [
    path('hello/', views.hello),
    path('grade/', views.grade),
    path('student/<int:id>/', views.students, name='student'),
    path('getip/', views.get_ip),
    path('login/', views.login),
    path('setcookie/', views.setcookie),
    path('mine/', views.mine, name='mine')
]
