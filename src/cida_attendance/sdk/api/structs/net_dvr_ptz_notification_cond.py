from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_NOTIFICATION_COND(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_NOTIFICATION_COND, [
    ('dwSize', DWORD),
    ('byEventType', WORD),
    ('byRes', BYTE * 2),
    ('dwChannel', DWORD),
    ('byRes1', BYTE * 128),
])

NET_DVR_PTZ_NOTIFICATION_COND = struct_tagNET_DVR_PTZ_NOTIFICATION_COND
LPNET_DVR_PTZ_NOTIFICATION_COND = POINTER(struct_tagNET_DVR_PTZ_NOTIFICATION_COND)
tagNET_DVR_PTZ_NOTIFICATION_COND = struct_tagNET_DVR_PTZ_NOTIFICATION_COND
