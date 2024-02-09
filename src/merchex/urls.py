"""
URL configuration for merchex project.

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
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
   
    path('',views.homePage, name="home"),
    path('bands/',views.band_list,name="band-list"),
    path('bands/<int:band_id>/',views.band_detail,name="band-detail"),
    path('bands/add/', views.band_create,name='band-create'),
    path('bands/<int:id>/change/',views.update_band, name="band-update"),
 
 

    path('listings/',views.lists,name="list-list"),
    path('listings/<int:list_id>/',views.list_detail,name="list-detail"),
    path('listings/add/',views.list_create,name='list-create'),
    path('listings/<int:id>/change/',views.update_listing,name='list-update'),
    
    path('contact/',views.contact,name="contact"),
    path('email/',views.email,name="email-sent")
   
]
