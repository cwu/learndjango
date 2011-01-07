from django.conf.urls.defaults import patterns

urlpatterns = patterns('learndjango.battle.views',
        (r'^(?P<battle_id>\d+)/$', 'battle'),
        (r'^new/$', 'new'),
        (r'^move/$', 'ajax_move'),
)
