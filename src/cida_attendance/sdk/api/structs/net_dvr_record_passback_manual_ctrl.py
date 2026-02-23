from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_CTRL(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_CTRL, [
    ('dwSize', DWORD),
    ('byControlType', BYTE),
    ('byRes', BYTE * 131),
])

NET_DVR_RECORD_PASSBACK_MANUAL_CTRL = struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_CTRL
LPNET_DVR_RECORD_PASSBACK_MANUAL_CTRL = POINTER(struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_CTRL)
tagNET_DVR_RECORD_PASSBACK_MANUAL_CTRL = struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_CTRL
