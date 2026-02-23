from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_54 import NET_DVR_PRESETCHAN_INFO
from .anon_55 import NET_DVR_CRUISECHAN_INFO
from .anon_56 import NET_DVR_PTZTRACKCHAN_INFO
from .net_dvr_handleexception_v41 import NET_DVR_HANDLEEXCEPTION_V41


class struct_tagNET_DVR_EVENT_TRIGGER(Structure):
    pass

_S(struct_tagNET_DVR_EVENT_TRIGGER, [
    ('dwSize', DWORD),
    ('struHandleException', NET_DVR_HANDLEEXCEPTION_V41),
    ('dwRelRecordChan', DWORD * 512),
    ('struPresetChanInfo', NET_DVR_PRESETCHAN_INFO * 512),
    ('struCruiseChanInfo', NET_DVR_CRUISECHAN_INFO * 512),
    ('struPtzTrackInfo', NET_DVR_PTZTRACKCHAN_INFO * 512),
    ('byDirection', BYTE),
    ('byRes2', BYTE * 255),
])

NET_DVR_EVENT_TRIGGER = struct_tagNET_DVR_EVENT_TRIGGER
LPNET_DVR_EVENT_TRIGGER = POINTER(struct_tagNET_DVR_EVENT_TRIGGER)
tagNET_DVR_EVENT_TRIGGER = struct_tagNET_DVR_EVENT_TRIGGER
