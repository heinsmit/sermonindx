from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.sermon_list_view, name='sermon_list'),
    url(r'^sermon/(?P<slug>[-\w]+)/$', views.sermon_detail_view, name='sermon_detail'),
    url(r'^speaker/(?P<slug>[-\w]+)/$', views.speaker_list_view, name='speaker_sermons_list'),
    url(r'^topic/(?P<slug>[-\w]+)/$', views.sermons_by_topic_view, name='topic_sermons_list'),
    url(r'^series/(?P<slug>[-\w]+)/$', views.series_sermons_view, name='series_sermons_list'),
]
