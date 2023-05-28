"""
URL configuration for WEventManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from WEventsMgmt import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('events/', views.eventsIndex),
    path('events/create/', views.createNewEvent),
    path('events/adduser/', views.addUserToEvent),
    path('users/', views.usersIndex),
    path('users/add/', views.addNewUser),
    path('api/users/', views.usersAPIView),
    path('api/users/<int:user_id>/', views.userDetailsAPIView),
    path('api/test1/', views.test1APIView),
    path('api/test2/<str:name>/', views.test2APIView),
    path('api/test3', views.test3APIView),
    path('api/test4', views.test4APIView),
    path('api/test5', views.test5APIView),
]
