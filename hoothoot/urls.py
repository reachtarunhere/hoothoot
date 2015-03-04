from django.conf.urls import patterns, include, url
from mainsite.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hoothoot.views.home', name='home'),
    # url(r'^hoothoot/', include('hoothoot.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^test/', latest_books),
     url(r'^ckeditor/', include('ckeditor.urls')),
    #mainsite urls
	url(r'', include('mainsite.urls')),
    url(r'^accounts/', include('allauth.urls')),
)
