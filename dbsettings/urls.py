from django.urls import re_path

from dbsettings.views import site_settings, app_settings


urlpatterns = [
    re_path(r'^$', site_settings, name='site_settings'),
    re_path(r'^(?P<app_label>[^/]+)/$', app_settings, name='app_settings'),
]
