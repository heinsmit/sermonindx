from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
# From CMS application
from cms.models import CMSPlugin
# From Filer application
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
# From CkEditor application
from djangocms_text_ckeditor.fields import HTMLField

# Create your models here.
class SermonIndxSermons(models.Model):
    si_title = models.CharField(
        verbose_name=_("Title"),
        max_length=200,
    )
    si_slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=50,
        db_index=True,
    )
    si_date = models.DateField(
        verbose_name=_("Sermon date"),
        blank=False,
        help_text=_("The date when the sermon was held."),
    )
    file_src = FilerFileField(
        verbose_name=_('Audio file'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    si_text = HTMLField(
        verbose_name=_("Text"),
        blank=True,
    )
    featured_image = FilerImageField(
        verbose_name=_('Featured image'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Prefered image size is: 600px(width) x 338px(height).",
        related_name='+',
    )
    si_bible_verse = models.CharField(
        verbose_name=_("Bible verse"),
        max_length=200,
        blank=True,
        null=True,
    )
    si_speaker = models.ForeignKey(
        "SermonIndxSpeakers",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name=_("Speaker"),
        related_name = 'sermons',
    )
    si_topic = models.ForeignKey(
        "SermonIndxTopics",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Topic"),
        related_name = 'sermons',
    )
    si_series = models.ForeignKey(
        "SermonIndxSeries",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Series"),
        related_name = 'sermons',
    )

    class Meta():
        verbose_name = _("Sermon")
        verbose_name_plural = _("Sermons")

    def __str__(self):
        return self.si_title


class SermonIndxSpeakers(models.Model):
    si_name = models.CharField(
        verbose_name=_("Name"),
        max_length=50,
        blank=False,
    )
    si_surname = models.CharField(
        verbose_name=_("Surname"),
        max_length=100,
        blank=False,
    )
    speaker_slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=50,
        db_index=True,
    )
    si_bio = HTMLField(
        verbose_name=_("Biography"),
        blank=True,
    )
    si_email =  models.EmailField(
        verbose_name=_("Email"),
        max_length=254,
        blank=True,
    )
    profile_image = FilerImageField(
        verbose_name=_('Profile image'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    class Meta():
        verbose_name = _("Speaker")
        verbose_name_plural = _("Speakers")

    def __str__(self):
        return "{name} {surname}".format(name=self.si_name, surname=self.si_surname)


class SermonIndxTopics(models.Model):
    si_topic = models.CharField(
        verbose_name=_("Topic name"),
        max_length=200,
        blank=False,
    )

    topic_slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=50,
        db_index=True,
    )

    class Meta():
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")

    def __str__(self):
        return self.si_topic


class SermonIndxSeries(CMSPlugin):
    si_series = models.CharField(
        verbose_name=_("Sermon series"),
        max_length=200,
        blank=False,
    )

    series_slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=50,
        db_index=True,
    )

    series_image = FilerImageField(
        verbose_name=_('Series image'),
        help_text=_("The image should be equal in width and height, image will be scaled in template."),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    series_excerpt = HTMLField(
        verbose_name=_("Excerpt"),
        blank=True,
    )

    class Meta():
        verbose_name = _("Series")
        verbose_name_plural = _("Series")

    def __str__(self):
        return self.si_series

class SermonPluginModel(CMSPlugin):
    sermon = models.ForeignKey(SermonIndxSermons)

    def __unicode__(self):
        return self.sermon.si_title
