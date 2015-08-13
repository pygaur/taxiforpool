try:
    from django.conf.urls.defaults import *
except ImportError:
    from django.conf.urls import *

urlpatterns = patterns('smart_selects.views',
    url(r'^filter/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<field>[\w\-]+)/$', 'filterchain', name='chained_filter'),
)
