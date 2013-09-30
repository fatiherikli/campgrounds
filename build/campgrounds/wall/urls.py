from django.conf.urls import patterns, url

from campgrounds.wall.views import WallDetailView


urlpatterns = patterns('',
    url(r'^(?P<content_type_id>\d+)/(?P<object_id>\d+)/$',
        WallDetailView.as_view(), name="wall-detail"),
)
