from plone.indexer.decorator import indexer
from tncr.content.interfaces import IMonument


@indexer(IMonument)
def dstrct(obj):
    try:
        head = obj.address.split(u'\u5340')[0]
        dstr = head.split(u'\u5e02')[1]
    except:
        return 'Unknown'
    return dstr + u'\u5340'

