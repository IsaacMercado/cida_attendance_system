from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_VIDEO_TRIGGER_COND(Structure):
    pass

_S(struct_tagNET_ITC_VIDEO_TRIGGER_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwTriggerMode', DWORD),
    ('byRes', BYTE * 16),
])

NET_ITC_VIDEO_TRIGGER_COND = struct_tagNET_ITC_VIDEO_TRIGGER_COND
LPNET_ITC_VIDEO_TRIGGER_COND = POINTER(struct_tagNET_ITC_VIDEO_TRIGGER_COND)
tagNET_ITC_VIDEO_TRIGGER_COND = struct_tagNET_ITC_VIDEO_TRIGGER_COND
