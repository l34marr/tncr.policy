from plone.indexer.decorator import indexer
from tncr.content.interfaces import IMonument
from tncr.content.interfaces import IRelic
from tncr.content.interfaces import IRuin
from tncr.content.interfaces import ILandscape
from tncr.content.interfaces import ISettlement
from tncr.content.interfaces import ITemple
from tncr.content.interfaces import IHouse
#from tncr.content.interfaces import ITree


def dstr(obj):
    try:
        head = obj.address.split(u'\u5340')[0]
        admn = head.split(u'\u5e02', 1)[1]
    except:
        return 'Unknown'
    if admn == u'\u6b78\u4ec1': return 'guiren'
    if admn == u'\u4e2d\u897f': return 'westcentral'
    if admn == u'\u5b89\u5357': return 'annan'
    if admn == u'\u5b89\u5e73': return 'anping'
    if admn == u'\u5357': return 'south'
    if admn == u'\u6771': return 'east'
    if admn == u'\u897f\u6e2f': return 'shigang'
    if admn == u'\u95dc\u5edf': return 'guanmiau'
    if admn == u'\u5927\u5167': return 'danei'
    if admn == u'\u5b98\u7530': return 'guantian'
    if admn == u'\u516d\u7532': return 'lioujia'
    if admn == u'\u6c38\u5eb7': return 'yungkang'
    if admn == u'\u6771\u5c71': return 'dungshan'
    if admn == u'\u9f8d\u5d0e': return 'lungchi'
    if admn == u'\u5f8c\u58c1': return 'houbi'
    if admn == u'\u67f3\u71df': return 'liouying'
    if admn == u'\u5b78\u7532': return 'shiuejia'
    if admn == u'\u5de6\u93ae': return 'tzuojen'
    if admn == u'\u5584\u5316': return 'shanhua'
    if admn == u'\u65b0\u5316': return 'sinhua'
    if admn == u'\u6960\u897f': return 'nanshi'
    if admn == u'\u5357\u5316': return 'nanhua'
    if admn == u'\u9ebb\u8c46': return 'madou'
    if admn == u'\u7389\u4e95': return 'yujing'
    if admn == u'\u767d\u6cb3': return 'baihe'
    if admn == u'\u5c71\u4e0a': return 'shanshang'
    if admn == u'\u5b89\u5b9a': return 'anding'
    if admn == u'\u65b0\u5e02': return 'sinshr'
    if admn == u'\u5317\u9580': return 'beimen'
    if admn == u'\u4f73\u91cc': return 'jiali'
    if admn == u'\u5c07\u8ecd': return 'jiangjiun'
    if admn == u'\u9e7d\u6c34': return 'yanshuei'
    if admn == u'\u4e03\u80a1': return 'chigu'
    if admn == u'\u65b0\u71df': return 'shinying'
    if admn == u'\u4ec1\u5fb7': return 'rende'
    if admn == u'\u5317': return 'north'
    if admn == u'\u4e0b\u71df': return 'shiaying'

@indexer(IMonument)
def dstrct_monument(obj):
    return dstr(obj)

@indexer(IRelic)
def dstrct_relic(obj):
    return dstr(obj)

@indexer(IRuin)
def dstrct_ruin(obj):
    return dstr(obj)

@indexer(ILandscape)
def dstrct_landscape(obj):
    return dstr(obj)

@indexer(ISettlement)
def dstrct_settlement(obj):
    return dstr(obj)

@indexer(ITemple)
def dstrct_temple(obj):
    return dstr(obj)

@indexer(IHouse)
def dstrct_house(obj):
    return dstr(obj)


def lvl(obj):
    if obj.level == u'\u570b\u5b9a':
        return 'ntnl'
    elif obj.level == u'\u76f4\u8f44\u5e02\u5b9a':
        return 'mncp'
    else:
        return None

@indexer(IMonument)
def level_monument(obj):
    return lvl(obj)

@indexer(IRelic)
def level_relic(obj):
    return lvl(obj)

@indexer(IRuin)
def level_ruin(obj):
    return lvl(obj)

@indexer(ILandscape)
def level_landscape(obj):
    return lvl(obj)

@indexer(ISettlement)
def level_settlement(obj):
    return lvl(obj)

@indexer(ITemple)
def level_temple(obj):
    return lvl(obj)

@indexer(IHouse)
def level_house(obj):
    return lvl(obj)

