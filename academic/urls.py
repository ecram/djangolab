from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('investigacion/', views.topics, name='topics'),
    path('areas/', views.areas, name='areas'),
	re_path(r'^contacto/$', views.contact, name='contact'),
	re_path(r'^premios/$', views.awards, name='awards'),
	re_path(r'^acerca/$', views.about, name='about'),
	re_path(r'^personal/$', views.people, name='people'),
    re_path(r'^proyectos/$', views.projects, name='projects'),
    re_path(r'^proyectos2/$', views.projects_details, name='projects_details'),
    re_path(r'^servicios/$', views.services, name='services'),
    re_path(r'^cursos/$', views.courses, name='courses'),
    re_path(r'^noticias/$', views.meetings, name='meetings'),
    re_path(r'^eventos/$', views.conferences, name='conferences'),
    re_path(r'^formularios/$', views.forms, name='forms'),
    re_path(r'^reportes/$', views.reports, name='reports'),
    re_path(r'^reportes/(?P<year>\w+)/$', views.reports, name='reports'),
    #re_path(r'^reportes/(?P<year>[0-9]+)/$', views.reports, name='reports'),
]
