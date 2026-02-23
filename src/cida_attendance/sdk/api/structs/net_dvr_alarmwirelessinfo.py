from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMWIRELESSINFO(Structure):
    pass

_S(struct_tagNET_DVR_ALARMWIRELESSINFO, [
    ('byDeviceID', BYTE * 32),
    ('fDataTraffic', c_float),
    ('bySignalIntensity', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_ALARMWIRELESSINFO = struct_tagNET_DVR_ALARMWIRELESSINFO
LPNET_DVR_ALARMWIRELESSINFO = POINTER(struct_tagNET_DVR_ALARMWIRELESSINFO)
tagNET_DVR_ALARMWIRELESSINFO = struct_tagNET_DVR_ALARMWIRELESSINFO
