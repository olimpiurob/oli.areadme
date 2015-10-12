from oli.areadme import _
from oli.areadme.interfaces import IAReadme
from plone.autoform import directives as form
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implements


class IAReadmeSchema(model.Schema):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    form.mode(data='hidden')
    data = schema.Text(
            title=_(u"Data"),
            required=False
        )


class AReadme(Item):
    implements(IAReadme)
