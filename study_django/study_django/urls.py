"""
Definition of urls for study_django.
"""

from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^webapp/', include('webapp.urls')),
	]

#it was here:
	#urlpatterns = patterns('',
	#    # Examples:
	#    # url(r'^$', 'study_django.views.home', name='home'),
	#    # url(r'^study_django/', include('study_django.study_django.urls')),

	#    # Uncomment the admin/doc line below to enable admin documentation:
	#    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	#    # Uncomment the next line to enable the admin:
	#    # url(r'^admin/', include(admin.site.urls)),
	#)
