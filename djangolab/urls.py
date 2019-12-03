"""djangolab URL Configuration

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
    1. Import the include() function: from

    xdcfvghbnjkml django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from django.conf import settings
from django.views.static import serve

from django.conf.urls import handler404, handler500

handler404 = 'academic.views.error404'
handler500 = 'academic.views.error500'

urlpatterns = [
	re_path(r'^publications/', include('publications.urls'), name='publications'),
    re_path(r'^', include('academic.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {
    	'document_root': settings.MEDIA_ROOT,}),
]
