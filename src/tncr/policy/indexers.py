from plone.indexer.decorator import indexer
from tncr.content.interfaces import IMonument
from tncr.content.interfaces import IRelic
from tncr.content.interfaces import IRuin
from tncr.content.interfaces import ILandscape
from tncr.content.interfaces import ISettlement
from tncr.content.interfaces import ITemple
from tncr.content.interfaces import IHouse
from tncr.content.interfaces import ITree


@indexer(IMonument)
def dstrct(obj):
    try:
        head = obj.address.split(u'\u5340')[0]
        dstr = head.split(u'\u5e02')[1]
    except:
        return 'Unknown'
    return dstr + u'\u5340'

@indexer(IRelic)
def dstrct(obj):
    try:
        head = obj.address.split(u'\u5340')[0]
        dstr = head.split(u'\u5e02')[1]
    except:
        return 'Unknown'
    return dstr + u'\u5340'

@indexer(IRuin)
def dstrct(obj):
    try:
        head = obj.address.split(u'\u5340')[0]
        dstr = head.split(u'\u5e02')[1]
    except:
        return 'Unknown'
    return dstr + u'\u5340'

@indexer(ILandscape)
def dstrct(obj):
    try:
        head = obj.address.split(u'\u5340')[0]
        dstr = head.split(u'\u5e02')[1]
    except:
        return 'Unknown'
    return dstr + u'\u5340'

@indexer(ITemple)
def dstrct(obj):
    try:
        head = obj.address.split(u'\u5340')[0]
        dstr = head.split(u'\u5e02')[1]
    except:
        return 'Unknown'
    return dstr + u'\u5340'

@indexer(IHouse)
def dstrct(obj):
    try:
        head = obj.address.split(u'\u5340')[0]
        dstr = head.split(u'\u5e02')[1]
    except:
        return 'Unknown'
    return dstr + u'\u5340'

@indexer(ITree)
def dstrct(obj):
    try:
        head = obj.address.split(u'\u5340')[0]
        dstr = head.split(u'\u5e02')[1]
    except:
        return 'Unknown'
    return dstr + u'\u5340'

