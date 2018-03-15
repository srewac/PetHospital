"""PetHospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from User import views as userviews
from Test import views as testviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', userviews.index, name='sign_in'),
    path('sign_up/', userviews.sign_up, name='sign_up'),
    path('sign_in/', userviews.sign_in, name='sign_in'),
    path('test/', testviews.test, name='test'),
    path('select_paper/', testviews.select_paper, name='select_paper'),
    path('test_management/', testviews.test_management, name='test_management'),
]

# 设置静态文件路径

