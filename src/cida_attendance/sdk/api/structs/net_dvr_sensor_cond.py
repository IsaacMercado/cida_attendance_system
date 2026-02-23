from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_historical_query_param import NET_DVR_HISTORICAL_QUERY_PARAM


class struct_tagNET_DVR_SENSOR_COND(Structure):
    pass

_S(struct_tagNET_DVR_SENSOR_COND, [
    ('dwSize', DWORD),
    ('byQueryType', BYTE),
    ('byDeviceType', BYTE),
    ('byDeviceID', BYTE),
    ('byRes1', BYTE),
    ('struHistoricalQueryParam', NET_DVR_HISTORICAL_QUERY_PARAM),
    ('byRes', BYTE * 64),
])

NET_DVR_SENSOR_COND = struct_tagNET_DVR_SENSOR_COND
LPNET_DVR_SENSOR_COND = POINTER(struct_tagNET_DVR_SENSOR_COND)
tagNET_DVR_SENSOR_COND = struct_tagNET_DVR_SENSOR_COND
