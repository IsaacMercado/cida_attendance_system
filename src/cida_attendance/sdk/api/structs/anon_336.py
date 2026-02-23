from ctypes import Union

from ..base_classes import _S
from .net_itc_polygon import NET_ITC_POLYGON
from .net_vca_rect import NET_VCA_RECT


class union_anon_336(Union):
    pass

_S(union_anon_336, [
    ('struRect', NET_VCA_RECT),
    ('struPolygon', NET_ITC_POLYGON),
])

