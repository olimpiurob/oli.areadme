""" View views for AReadme
"""

from Products.Five import BrowserView
from zope.component import getMultiAdapter
from zope.component import ComponentLookupError


class AReadmeView(BrowserView):
    """ AReadmeView view
    """

    def get_tinymce_options(self):
        """
        We're just going to be looking up settings from
        plone pattern options
        """
        args = {'pattern_options': {}}
        try:
            pattern_options = getMultiAdapter(
                (self.context, self.request, None),
                name="plone_settings").tinymce()['data-pat-tinymce']
            args = pattern_options
        except (ComponentLookupError, AttributeError):
            pass

        return args
