"""Jango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('app/', include(('app.urls', 'app'), namespace='app')),
    path('two/', include(('Two.urls', 'Two'), namespace='two')),
    path('three/', include(('three.urls', 'three'), namespace='three')),
=======
    path('app/', include('app.urls')),
    path('paginator/', include(('paginator_app.urls', 'paginator_app'), namespace='paginator')),
    path('verify/', include(('verify_code.urls', 'verify_code'), namespace='verify')),
>>>>>>> 750569be8370ed206f930d91d6e8d31fd4a2e3a8
]
