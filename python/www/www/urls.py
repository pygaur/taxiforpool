from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',

    url(r'^', include('taxi_ui.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
)
