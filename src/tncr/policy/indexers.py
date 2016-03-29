from plone.indexer.decorator import indexer
from tncr.content.interfaces import IMonument


@indexer(IMonument)
def district(obj):
    try:
        head = obj.address.split(u'\u5340')[0]
        dist = head.split(u'\u5e02')[1]
    except:
        return 'Unknown'
    return dist + u'\u5340'

