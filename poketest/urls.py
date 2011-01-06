from django.conf.urls.defaults import patterns

urlpatterns = patterns('learndjango.poketest.views',
        (r'^pokedex/$', 'pokedex_show'),
        (r'^pokedex/(?P<name>.+)/$', 'pokedex_lookup'),
)

