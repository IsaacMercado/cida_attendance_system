from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_flashout_info import NET_ITC_FLASHOUT_INFO
from .net_itc_serial_checkinfo import NET_ITC_SERIAL_CHECKINFO
from .net_itc_traffic_light_color import NET_ITC_TRAFFIC_LIGHT_COLOR
from .net_itc_traffic_light_turn import NET_ITC_TRAFFIC_LIGHT_TURN
from .net_itc_triggerio_info import NET_ITC_TRIGGERIO_INFO
from .net_itc_triggertype_info import NET_ITC_TRIGGERTYPE_INFO


class union_tagNET_ITC_STATUS_UNION(Union):
    pass

_S(union_tagNET_ITC_STATUS_UNION, [
    ('uLen', BYTE * 48),
    ('struTrigIO', NET_ITC_TRIGGERIO_INFO),
    ('struFlashOut', NET_ITC_FLASHOUT_INFO),
    ('struSerial', NET_ITC_SERIAL_CHECKINFO),
    ('struTrigType', NET_ITC_TRIGGERTYPE_INFO),
    ('struTrafficLightColor', NET_ITC_TRAFFIC_LIGHT_COLOR),
    ('struTrafficLightTurn', NET_ITC_TRAFFIC_LIGHT_TURN),
])

NET_ITC_STATUS_UNION = union_tagNET_ITC_STATUS_UNION
LPNET_ITC_STATUS_UNION = POINTER(union_tagNET_ITC_STATUS_UNION)
tagNET_ITC_STATUS_UNION = union_tagNET_ITC_STATUS_UNION
