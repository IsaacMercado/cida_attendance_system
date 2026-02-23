from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PUSHALARMINFO(Structure):
    pass

_S(struct_tagNET_DVR_PUSHALARMINFO, [
    ('dwAlarmType', DWORD),
    ('dwAlarmInputNumber', DWORD),
    ('dwAlarmOutputNumber', DWORD * 4),
    ('dwAlarmRelateChannel', DWORD * 16),
    ('dwChannel', DWORD * 16),
    ('dwDiskNumber', DWORD * 16),
    ('byDeviceID', BYTE * 32),
    ('byRes', BYTE * 4),
])

NET_DVR_PUSHALARMINFO = struct_tagNET_DVR_PUSHALARMINFO
LPNET_DVR_PUSHALARMINFO = POINTER(struct_tagNET_DVR_PUSHALARMINFO)
tagNET_DVR_PUSHALARMINFO = struct_tagNET_DVR_PUSHALARMINFO
