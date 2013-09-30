from django import forms

from campgrounds.places.models import Campground, Feature


class NewCampgroundForm(forms.ModelForm):
    features = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Feature.objects.all(),
        required=False)

    class Meta:
        model = Campground
        fields = (
            "title", "city", "location", "directions", "description", "image",
            "features")

    def save(self, commit=True):
        slug = Campground.unique_slug(self.instance.title)
        self.instance.slug = slug
        return super(NewCampgroundForm, self).save(commit)
