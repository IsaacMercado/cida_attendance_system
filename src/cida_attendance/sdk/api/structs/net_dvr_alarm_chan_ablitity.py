from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARM_CHAN_ABLITITY(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_CHAN_ABLITITY, [
    ('dwSize', DWORD),
    ('bySensorChan', BYTE * 64),
    ('byAlarmInChan', BYTE * 64),
    ('byAlarmOutChan', BYTE * 64),
    ('by485Chan', BYTE * 64),
    ('byRes', BYTE * 128),
])

NET_DVR_ALARM_CHAN_ABLITITY = struct_tagNET_DVR_ALARM_CHAN_ABLITITY
LPNET_DVR_ALARM_CHAN_ABLITITY = POINTER(struct_tagNET_DVR_ALARM_CHAN_ABLITITY)
tagNET_DVR_ALARM_CHAN_ABLITITY = struct_tagNET_DVR_ALARM_CHAN_ABLITITY
