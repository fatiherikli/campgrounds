import json
from itertools import imap

from django.templatetags.static import static
from django.views.generic import ListView, DetailView

from campgrounds.places.mixins import JSONResponseMixin
from campgrounds.places.models import Campground


class CampgroundList(JSONResponseMixin, ListView):
    model = Campground

    def convert_context_to_json(self, context):
        return json.dumps(list(imap(
            self.build_bundle, context['object_list'])))

    def build_bundle(self, place):
        """Builds json bundle for api response"""
        return {
            "id": place.id,
            "title": place.title,
            "city": place.city,
            "image": static(place.image.url),
            "url": place.get_absolute_url(),
            "coordinates": {
                "latitude": place.location.y,
                "longitude": place.location.x
            },
        }


class CampgroundDetail(DetailView):
    template_name = "places/detail.html"
    model = Campground
    context_object_name = "place"
