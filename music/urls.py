"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from music_app import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music_app/login/', views.login),
    path('music_app/songs/', views.songs_list),
    path('music_app/songs/<int:pk>/', views.songs_detail),
    path('music_app/playlists/', views.playlists_list),
    path('music_app/playlists/<int:pk>/', views.playlists_detail),
    path('music_app/ratings/', views.ratings_list),
    path('music_app/ratings/<int:pk>/', views.ratings_detail),
    url(r'^music_app/search/$', views.search),
#    path('', include('music.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
