from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^$', view=views.search_page,name='index'),
    url(regex=r'^submit/$', view=views.get_query,name='query'),
    url(regex=r'^(?P<query>\w{0,50})/$', view=views.search,name='search'),

    ]