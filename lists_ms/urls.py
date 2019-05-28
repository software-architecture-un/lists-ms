"""lists_ms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from lists_ms.lists_ms.views import *

# list_list= views.ListViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# list_places = views.ListViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^lists-ms/list/(?P<pk>[0-9]+)$', lists), # GET-PUT-DELETE lists
    url(r'^lists-ms/place/(?P<pk>[0-9]+)$', place), # GET-PUT-DELETE place
    url(r'^lists-ms/list$', lists_create), # POST lists
    url(r'^lists-ms/place$', place_create), #POST place
    url(r'^lists-ms/lists/(?P<pk>[0-9]+)$', lists_by_user), 
    url(r'^lists-ms/list_all/(?P<pk>[0-9]+)$', list_with_places_by_list),
    url(r'^lists-ms/places/(?P<pk>[0-9]+)$', places_by_list),
    
]
