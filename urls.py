from django.conf.urls.defaults import *

import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^media/(?P<path>.*)$', 
     'django.views.static.serve', 
     {'document_root': settings.MEDIA_ROOT}
     ),

    (r'^tinymce/', include('tinymce.urls')),


    (r'^admin/filebrowser/', 
     include('filebrowser.urls')
     ),
     
    (r'^admin/', 
     include(admin.site.urls)
     ),
     
     
    (r'^$',
     'app.views.getContent', 
     {'template': 'index.html', 
      }
     ),
)