from django.conf.urls.defaults import patterns

urlpatterns = patterns('learndjango.poketest.views',
        (r'^trainer/new/$', 'new_trainer'),
        (r'^trainer/(?P<name>.+)/$', 'show_trainer'),
        (r'^trainer/$', 'show_trainer'),
)

