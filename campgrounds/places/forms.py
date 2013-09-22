from django import forms
from django.utils.text import slugify

from campgrounds.places.models import Campground, Feature


class NewCampgroundView(forms.ModelForm):
    features = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Feature.objects.all())

    class Meta:
        model = Campground
        fields = (
            "title", "city", "location", "directions", "image", "features")

    def save(self, commit=True):
        self.instance.slug = slugify(self.instance.title)
        return super(NewCampgroundView, self).save(commit)
