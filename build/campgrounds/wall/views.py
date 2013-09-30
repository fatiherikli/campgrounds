from django.shortcuts import redirect
from django.views.generic import ListView

from campgrounds.wall.forms import SubmitToWallForm
from campgrounds.wall.models import Entry


class WallDetailView(ListView):
    model = Entry

    def get_queryset(self):
        return super(WallDetailView, self).get_queryset().filter(
            content_type_id=self.kwargs.get('content_type_id'),
            object_id=self.kwargs.get('object_id')
        )

    def post(self, request, content_type_id, object_id):
        # todo: add validation
        # todo: encapsulate redirect and error urls
        # todo: reach the real object with content type and object id
        form = SubmitToWallForm(request.POST)
        if not form.is_valid():
            return request.META.get('HTTP_REFERER')
        form.instance.content_type_id = content_type_id
        form.instance.object_id = object_id
        form.instance.user = request.user
        form.save()
        return redirect(request.META.get('HTTP_REFERER'))
