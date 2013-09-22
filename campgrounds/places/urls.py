from django.conf.urls import patterns, url

from campgrounds.places.views import CampgroundList, CampgroundDetail, NewCampground


urlpatterns = patterns('',
    url(r'^$', CampgroundList.as_view()),
    url(r'^new$', NewCampground.as_view(), name="new-place"),
    url(r'^(?P<slug>[-\w]+)/$', CampgroundDetail.as_view(), name="place-detail"),
)
