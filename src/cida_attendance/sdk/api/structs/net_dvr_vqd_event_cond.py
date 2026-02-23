from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VQD_EVENT_COND(Structure):
    pass

_S(struct_tagNET_DVR_VQD_EVENT_COND, [
    ('dwChannel', DWORD),
    ('dwEventType', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_VQD_EVENT_COND = struct_tagNET_DVR_VQD_EVENT_COND
LPNET_DVR_VQD_EVENT_COND = POINTER(struct_tagNET_DVR_VQD_EVENT_COND)
tagNET_DVR_VQD_EVENT_COND = struct_tagNET_DVR_VQD_EVENT_COND
