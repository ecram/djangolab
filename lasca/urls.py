from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('academic.urls')),
	url(r'^publications/', include('publications.urls')),
	url(r'^admin_django_lab/publications/publication/import_bibtex/$', 'publications.admin_views.import_bibtex'),
    url(r'^admin_django_lab/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)

urlpatterns += patterns('',
                    url(r'^media/(?P<path>.*)$',
'django.views.static.serve', {'document_root':'./media/'}),
                    )

handler404 = 'academic.views.error404'
handler500 = 'academic.views.error500'
