from eea.faceted.vocabularies.utils import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from tncr.policy import _


class CrTypes(object):
    """Vocabulary Factory for Cultural Resource Types.
    """
    implements(IVocabularyFactory)

    def __call__(self, context=None):
        items = (
            SimpleTerm(value='Monument', title=_(u'Monument')),
            SimpleTerm(value='Relic', title=_(u'Relic')),
            SimpleTerm(value='Ruin', title=_(u'Ruin')),
            SimpleTerm(value='Landscape', title=_(u'Landscape')),
            SimpleTerm(value='Settlement', title=_(u'Settlement')),
            SimpleTerm(value='Temple', title=_(u'Temple')),
            SimpleTerm(value='House', title=_(u'House')),
            SimpleTerm(value='Tree', title=_(u'Tree'))
        )
        return SimpleVocabulary(items)

class CrLevel(object):
    """Vocabulary Factory for Cultural Resource Level.
    """
    implements(IVocabularyFactory)

    def __call__(self, context=None):
        items = (
            SimpleTerm(value='ntnl', title=_(u'National')),
            SimpleTerm(value='mncp', title=_(u'Municipal'))
        )
        return SimpleVocabulary(items)

