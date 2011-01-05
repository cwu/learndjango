from django.conf.urls.defaults import patterns

urlpatterns = patterns('dahsboard.poketest.views',
        (r'^show/(\d+)/$', show),
)
