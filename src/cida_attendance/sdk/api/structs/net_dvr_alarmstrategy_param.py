from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMSTRATEGY_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_ALARMSTRATEGY_PARAM, [
    ('byStrategyType', BYTE),
    ('byRes', BYTE * 15),
])

NET_DVR_ALARMSTRATEGY_PARAM = struct_tagNET_DVR_ALARMSTRATEGY_PARAM
LPNET_DVR_ALARMSTRATEGY_PARAM = POINTER(struct_tagNET_DVR_ALARMSTRATEGY_PARAM)
tagNET_DVR_ALARMSTRATEGY_PARAM = struct_tagNET_DVR_ALARMSTRATEGY_PARAM
