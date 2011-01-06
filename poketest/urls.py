from django.conf.urls.defaults import patterns

urlpatterns = patterns('learndjango.poketest.views',
        (r'^battle/$', 'poke_battle'),
        (r'^trainer/new/$', 'new_trainer'),
        (r'^trainer/(?P<name>.+)/$', 'show_trainer'),
)

