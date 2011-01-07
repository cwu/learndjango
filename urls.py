from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^learndjango/', include('learndjango.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^accounts/login/', login),
    (r'^accounts/logout/', logout),
    (r'^accounts/profile$', 'django.views.generic.simple.redirect_to', { 'url' : '/trainer' }),

    (r'^login/$', 'django.views.generic.simple.redirect_to', { 'url' : '/accounts/login' }),
    (r'^logout/$', 'django.views.generic.simple.redirect_to', { 'url' : '/accounts/logout' }),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^poke/', include('learndjango.poketest.urls')),
    (r'^pokedex/', include('learndjango.pokedex.urls')),
    (r'^battle/', include('learndjango.battle.urls')),
    
)

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
        { 'document_root': settings.STATIC_DOC_ROOT,
              'show_indexes': True
            }),)
