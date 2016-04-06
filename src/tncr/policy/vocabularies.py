# -*- coding: utf-8 -*-

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

class TnDstrct(object):
    """Vocabulary Factory for Tainan Adm District.
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='guiren', title=_(u'歸仁區')),
            SimpleTerm(value='westcentral', title=_(u'中西區')),
            SimpleTerm(value='annan', title=_(u'安南區')),
            SimpleTerm(value='anping', title=_(u'安平區')),
            SimpleTerm(value='south', title=_(u'南區')),
            SimpleTerm(value='east', title=_(u'東區')),
            SimpleTerm(value='shigang', title=_(u'西港區')),
            SimpleTerm(value='guanmiau', title=_(u'關廟區')),
            SimpleTerm(value='danei', title=_(u'大內區')),
            SimpleTerm(value='guantian', title=_(u'官田區')),
            SimpleTerm(value='lioujia', title=_(u'六甲區')),
            SimpleTerm(value='yungkang', title=_(u'永康區')),
            SimpleTerm(value='dungshan', title=_(u'東山區')),
            SimpleTerm(value='lungchi', title=_(u'龍崎區')),
            SimpleTerm(value='houbi', title=_(u'後壁區')),
            SimpleTerm(value='liouying', title=_(u'柳營區')),
            SimpleTerm(value='shiuejia', title=_(u'學甲區')),
            SimpleTerm(value='tzuojen', title=_(u'左鎮區')),
            SimpleTerm(value='shanhua', title=_(u'善化區')),
            SimpleTerm(value='sinhua', title=_(u'新化區')),
            SimpleTerm(value='nanshi', title=_(u'楠西區')),
            SimpleTerm(value='nanhua', title=_(u'南化區')),
            SimpleTerm(value='madou', title=_(u'麻豆區')),
            SimpleTerm(value='yujing', title=_(u'玉井區')),
            SimpleTerm(value='baihe', title=_(u'白河區')),
            SimpleTerm(value='shanshang', title=_(u'山上區')),
            SimpleTerm(value='anding', title=_(u'安定區')),
            SimpleTerm(value='shinshr', title=_(u'新市區')),
            SimpleTerm(value='beimen', title=_(u'北門區')),
            SimpleTerm(value='jiali', title=_(u'佳里區')),
            SimpleTerm(value='jiangjiun', title=_(u'將軍區')),
            SimpleTerm(value='yanshuei', title=_(u'鹽水區')),
            SimpleTerm(value='chigu', title=_(u'七股區')),
            SimpleTerm(value='shinying', title=_(u'新營區')),
            SimpleTerm(value='rende', title=_(u'仁德區')),
            SimpleTerm(value='north', title=_(u'北區')),
            SimpleTerm(value='shiaying', title=_(u'下營區')),
        )
        return SimpleVocabulary(items)

