from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_alarmhost_point_value import NET_DVR_ALARMHOST_POINT_VALUE


class union_tagNET_DVR_ALARMHOST_DATA_UNION(Union):
    pass

_S(union_tagNET_DVR_ALARMHOST_DATA_UNION, [
    ('byLength', BYTE * 40),
    ('struPointValue', NET_DVR_ALARMHOST_POINT_VALUE),
])

NET_DVR_ALARMHOST_DATA_UNION = union_tagNET_DVR_ALARMHOST_DATA_UNION
LPNET_DVR_ALARMHOST_DATA_UNION = POINTER(union_tagNET_DVR_ALARMHOST_DATA_UNION)
tagNET_DVR_ALARMHOST_DATA_UNION = union_tagNET_DVR_ALARMHOST_DATA_UNION
