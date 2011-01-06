from django.conf.urls.defaults import patterns

urlpatterns = patterns('learndjango.pokedex.views',
        (r'^(?P<name>.+)/$', 'lookup'),
        (r'$', 'show'),
)

