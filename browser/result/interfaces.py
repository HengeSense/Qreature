# -*- coding: cp1251 -*-

from zope.interface import Interface
from zope.schema import Int

class IInterval(Interface):
    pass

class Interval(Int):
    pass
    
class IResultInterval(Interface):
    interval = Interval(title=u'�����.�������:')

class IResultIntervalForm(Interface):
    pass
