from django.conf.urls.defaults import patterns

urlpatterns = patterns('learndjango.battle.views',
        (r'^$', 'battle'),
)
