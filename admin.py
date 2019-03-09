from django.contrib import admin

from .models import SermonIndxSermons
from .models import SermonIndxSpeakers
from .models import SermonIndxTopics
from .models import SermonIndxSeries

class SermonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"si_slug": ("si_title",)}

class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"series_slug": ("si_series",)}

class TopicsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"topic_slug": ("si_topic",)}

class SpeakersAdmin(admin.ModelAdmin):
    prepopulated_fields = {"speaker_slug": ("si_name",)}

# Register your models here.
admin.site.register(SermonIndxSermons, SermonAdmin)
admin.site.register(SermonIndxSpeakers, SpeakersAdmin)
admin.site.register(SermonIndxTopics, TopicsAdmin)
admin.site.register(SermonIndxSeries, SeriesAdmin)
