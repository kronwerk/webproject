from django.conf.urls.defaults import patterns, include, url
from polls import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^date$', views.current_datetime),
    # Examples:
    # url(r'^$', 'djangoapp.views.home', name='home'),
    # url(r'^djangoapp/', include('djangoapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
