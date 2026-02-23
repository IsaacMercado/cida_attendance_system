from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_189(Structure):
    pass

_S(struct_anon_189, [
    ('sSerialNumber', BYTE * 48),
    ('byAlarmInPortNum', BYTE),
    ('byAlarmOutPortNum', BYTE),
    ('byDiskNum', BYTE),
    ('byDVRType', BYTE),
    ('byChanNum', BYTE),
    ('byStartChan', BYTE),
])

NET_DVR_DEVICEINFO = struct_anon_189
LPNET_DVR_DEVICEINFO = POINTER(struct_anon_189)
