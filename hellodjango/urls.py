from django.conf.urls import patterns, include, url
from writer.views import EmailInput
from django.conf import settings
from search.views import search_form, search
from parallax.views import pageload


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# url(r'^/', 'writer.views.EmailInput'),
    url(r'^search-form/$', 'search.views.search_form'),
    (r'^search/$', 'search.views.search'),
    url(r'home','parallax.views.pageload'),

    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^hellodjango/', include('hellodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
# if not settings.DEBUG:
#     urlpatterns += patterns('',
#         (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#     )