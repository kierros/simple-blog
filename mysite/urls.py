from django.conf.urls import include, url
import django.contrib.auth.views

from django.contrib import admin
from django.conf.urls import handler404

#, handler403, handler400, handler500

#handler400 = 'blog.views.bad_request'
#handler403 = 'blog.views.permission_denied'
handler404 = 'blog.views.page_not_found'
#handler500 = 'blog.views.server_error'


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
    url(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('blog.urls')),
]
