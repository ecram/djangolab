from django.conf.urls import patterns, url
from academic import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^people/$', views.people, name='people'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^meetings/$', views.meetings, name='meetings'),
    url(r'^conferences/$', views.conferences, name='conferences'),
    url(r'^awards/$', views.awards, name='awards'),
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^reports/(?P<year>\w+)/$', views.reports, name='reports'),
    )
