from django.conf.urls.defaults import patterns

urlpatterns = patterns('learndjango.poketest.views',
        (r'^pokedex/$', 'pokedex_show'),
        (r'^pokedex/(?P<name>\w+)/$', 'pokedex_lookup'),
)

