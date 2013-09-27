# coding=utf-8
import json
from itertools import imap
from django.contrib import messages
from django.shortcuts import redirect

from django.templatetags.static import static
from django.views.generic import ListView, DetailView, CreateView

from campgrounds.places.forms import NewCampgroundForm
from campgrounds.places.mixins import JSONResponseMixin
from campgrounds.places.models import Campground


class CampgroundList(JSONResponseMixin, ListView):
    queryset = Campground.objects.active()

    def convert_context_to_json(self, context):
        return json.dumps(list(imap(
            self.build_bundle, context['object_list'])))

    def build_bundle(self, place):
        """Builds json bundle for api response"""
        try:
            image = static(place.image.url)
        except ValueError:
            image = None

        return {
            "id": place.id,
            "title": place.title,
            "city": place.city,
            "image": image,
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

    def post(self, request, slug):
        if 'stay' in request.POST:
            campground = self.get_object()
            people = campground.people_who_stay
            if request.user in people.all():
                people.remove(request.user)
                messages.info(request, 'Topluluktan ayrıldınız.')
            else:
                people.add(request.user)
                messages.info(request, 'Topluluğa katıldınız.')

            return redirect(campground)
        return self.get(request, slug)


class NewCampground(CreateView):
    model = Campground
    form_class = NewCampgroundForm
    template_name = "places/new.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.info(self.request, 'Kamp alanı başarıyla eklendi. Editörler '
                                    'tarafından onaylandıktan sonra harita '
                                    'üzerinde gözükecektir. Teşekkür ederiz.')
        return super(NewCampground, self).form_valid(form)
