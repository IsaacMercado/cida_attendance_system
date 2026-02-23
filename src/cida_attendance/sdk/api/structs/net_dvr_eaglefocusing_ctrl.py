from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EAGLEFOCUSING_CTRL(Structure):
    pass

_S(struct_tagNET_DVR_EAGLEFOCUSING_CTRL, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byHeightCompensationEnable', BYTE),
    ('byHeightCompensationValue', BYTE),
    ('byRes', BYTE * 509),
])

NET_DVR_EAGLEFOCUSING_CTRL = struct_tagNET_DVR_EAGLEFOCUSING_CTRL
LPNET_DVR_EAGLEFOCUSING_CTRL = POINTER(struct_tagNET_DVR_EAGLEFOCUSING_CTRL)
tagNET_DVR_EAGLEFOCUSING_CTRL = struct_tagNET_DVR_EAGLEFOCUSING_CTRL
