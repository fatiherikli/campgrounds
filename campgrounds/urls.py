from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.contrib.auth.views import logout
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(
        template_name="places/index.html"), name='home'),
    url(r'^detail.html$', TemplateView.as_view(
        template_name="detail.html"), name='home'),
    url(r'logout$', logout,  {'next_page': "/"}, name='logout'),
    url(r'^places/', include('campgrounds.places.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
)
