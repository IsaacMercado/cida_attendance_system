from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_system_time import NET_DVR_SYSTEM_TIME


class struct_tagNET_ITS_TRAFFIC_DATA_INFO(Structure):
    pass

_S(struct_tagNET_ITS_TRAFFIC_DATA_INFO, [
    ('dwDataQuantity', DWORD),
    ('dwDataRsendQuantity', DWORD),
    ('struStartTime', NET_DVR_SYSTEM_TIME),
    ('struEndTime', NET_DVR_SYSTEM_TIME),
    ('struDataHost', NET_DVR_IPADDR),
])

NET_ITS_TRAFFIC_DATA_INFO = struct_tagNET_ITS_TRAFFIC_DATA_INFO
LPNET_ITS_TRAFFIC_DATA_INFO = POINTER(struct_tagNET_ITS_TRAFFIC_DATA_INFO)
tagNET_ITS_TRAFFIC_DATA_INFO = struct_tagNET_ITS_TRAFFIC_DATA_INFO
