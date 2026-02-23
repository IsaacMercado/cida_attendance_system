from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_event_info import NET_DVR_EVENT_INFO


class struct_tagNET_DVR_EVENT_INFO_LIST(Structure):
    pass

_S(struct_tagNET_DVR_EVENT_INFO_LIST, [
    ('byNum', BYTE),
    ('byRes1', BYTE * 3),
    ('struEventInfo', NET_DVR_EVENT_INFO * 8),
])

NET_DVR_EVENT_INFO_LIST = struct_tagNET_DVR_EVENT_INFO_LIST
LPNET_DVR_EVENT_INFO_LIST = POINTER(struct_tagNET_DVR_EVENT_INFO_LIST)
tagNET_DVR_EVENT_INFO_LIST = struct_tagNET_DVR_EVENT_INFO_LIST
