from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()
 
urlpatterns = patterns('',

    (r'^monit/', include('monit.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
 
)

