from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CLEARCTRL(Structure):
    pass

_S(struct_tagNET_DVR_CLEARCTRL, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('byAllPreset', BYTE),
    ('byAllPatrols', BYTE),
    ('byAllPatterms', BYTE),
    ('byAllPrivacyMasks', BYTE),
    ('byAllPTZLimited', BYTE),
    ('byAllScheduledTasks', BYTE),
    ('byAllParkAction', BYTE),
    ('byRes', BYTE * 125),
])

NET_DVR_CLEARCTRL = struct_tagNET_DVR_CLEARCTRL
LPNET_DVR_CLEARCTRL = POINTER(struct_tagNET_DVR_CLEARCTRL)
tagNET_DVR_CLEARCTRL = struct_tagNET_DVR_CLEARCTRL
