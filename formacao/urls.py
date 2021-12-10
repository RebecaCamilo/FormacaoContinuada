"""formacao URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from accounts.api import viewsets as accountsviewsets
from courses.api import viewsets as coursesviewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


route = routers.DefaultRouter()
route.register(r'register', accountsviewsets.RegisterViewSet, basename="register")
route.register(r'courses', coursesviewsets.CourseViewSet, basename="courses")
route.register(r'lesson', coursesviewsets.LessonViewSet, basename="lessons")
route.register(r'materials', coursesviewsets.MaterialViewSet, basename="materials")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')), #acesso a tela de login entre outras do django rest framework
    ##### AUTHENTICATION JWT ##################
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    ##### ENDPOINTS PARA GENERICS CLASSES ############
    #path("generics-get-post/", accountsviewsets.RegisterListCreateGenerics.as_view(), name=""),
    #path("get/", accountsviewsets.RegisterListGenerics.as_view(), name=""),
    #path("post/", accountsviewsets.RegisterCreateGenerics.as_view(), name=""),
]

