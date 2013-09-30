from django import forms

from campgrounds.wall.models import Entry


class SubmitToWallForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['entry_type', 'content', 'image', 'link']
