from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

@apphook_pool.register
class SermonIndxApphook(CMSApp):
    app_name = "sermonindx"
    name = _("Sermon Indx")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["sermonindx.urls"]
