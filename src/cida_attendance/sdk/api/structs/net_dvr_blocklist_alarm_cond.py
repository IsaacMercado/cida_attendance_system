from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BLOCKLIST_ALARM_COND(Structure):
    pass

_S(struct_tagNET_DVR_BLOCKLIST_ALARM_COND, [
    ('dwSize', DWORD),
    ('byType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwFaceID', DWORD),
    ('dwMaxSnapNum', DWORD),
    ('byRes', BYTE * 256),
])

NET_DVR_BLOCKLIST_ALARM_COND = struct_tagNET_DVR_BLOCKLIST_ALARM_COND
LPNET_DVR_BLOCKLIST_ALARM_COND = POINTER(struct_tagNET_DVR_BLOCKLIST_ALARM_COND)
tagNET_DVR_BLOCKLIST_ALARM_COND = struct_tagNET_DVR_BLOCKLIST_ALARM_COND
