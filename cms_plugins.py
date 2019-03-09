from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models import CMSPlugin
from django.utils.translation import ugettext as _

from .models import SermonPluginModel, SermonIndxSpeakers, SermonIndxTopics, SermonIndxSeries

@plugin_pool.register_plugin
class SermonPluginPublisher(CMSPluginBase):
    model = SermonPluginModel
    module = _("SermonIndx")
    name = _("Sermon Plugin")
    render_template = "sermonindx/plugins/sermon.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin
class SpeakersPluginWidget(CMSPluginBase):
    model = CMSPlugin
    module = _("SermonIndx")
    name = _("Speakers Plugin")
    render_template = "sermonindx/plugins/speakers.html"

    def render(self, context, instance, placeholder):
        context = super(SpeakersPluginWidget, self).render(context, instance, placeholder)
        context.update({
            'speakers': SermonIndxSpeakers.objects.all().order_by("si_name"),
        })
        return context

@plugin_pool.register_plugin
class TopicsPluginWidget(CMSPluginBase):
    model = CMSPlugin
    module = _("SermonIndx")
    name = _("Topics Plugin")
    render_template = "sermonindx/plugins/topics.html"

    def render(self, context, instance, placeholder):
        context = super(TopicsPluginWidget, self).render(context, instance, placeholder)
        context.update({
            'topics': SermonIndxTopics.objects.all().order_by("si_topic"),
        })
        return context

@plugin_pool.register_plugin
class SeriesPluginWidget(CMSPluginBase):
    model = CMSPlugin
    module = _("SermonIndx")
    name = _("Series Plugin")
    render_template = "sermonindx/plugins/series.html"

    def render(self, context, instance, placeholder):
        context = super(SeriesPluginWidget, self).render(context, instance, placeholder)
        context.update({
            'series': SermonIndxSeries.objects.all().order_by('si_series')
        })
        return context