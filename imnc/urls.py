"""imnc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # www.xxx.com/index/ -> 函数
    path('index/', views.index, name='index'),

    path('index/scene/about/', views.about, name='about'),

    path('index/blog/blog/', views.blog, name='blog'),

    path('scene/profile/', views.profile, name='profile'),

    path('blog/jishu1/', views.jishu1, name='jishu1'),

    path('blog/jishu2/', views.jishu2, name='jishu2'),

    path('blog/jishu3/', views.jishu3, name='jishu3'),

    path('blog/Author/', views.Author, name='author'),

    path('link/link/', views.link, name="link"),

    path('scene/digital/', views.digital, name="digital"),

    path('scene/front/', views.front, name="front"),

    path('scene/rear/', views.rear, name="rear"),

    path('scene/service/', views.service, name="service"),

    path('scene/AI/', views.AI, name="AI"),

    path('login/', views.login, name="login"),

    path('regist/', views.regist, name="regist"),

    path('loginout/', views.loginout, name="loginout"),

    path('face_login/', views.face_login, name="face_login"),

    # path('login/face_response', views.face_response, name="face_response"),

    path('face/face_regist', views.faceReg, name="faceReg"),

    path('face_reg/', views.face_reg, name="face_reg"),

    path('user/user_list/', views.user_list, name="user_list")



]
