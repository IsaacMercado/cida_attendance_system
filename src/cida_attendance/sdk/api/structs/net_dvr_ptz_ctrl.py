from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_CTRL(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_CTRL, [
    ('byEnable', BYTE),
    ('byType', BYTE),
    ('byPtzNo', BYTE),
    ('byRes', BYTE * 5),
])

NET_DVR_PTZ_CTRL = struct_tagNET_DVR_PTZ_CTRL
LPNET_DVR_PTZ_CTRL = POINTER(struct_tagNET_DVR_PTZ_CTRL)
tagNET_DVR_PTZ_CTRL = struct_tagNET_DVR_PTZ_CTRL
