from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INPUT_INTERFACE_CTRL(Structure):
    pass

_S(struct_tagNET_DVR_INPUT_INTERFACE_CTRL, [
    ('byInputSourceType', BYTE),
    ('byRes', BYTE * 15),
])

NET_DVR_INPUT_INTERFACE_CTRL = struct_tagNET_DVR_INPUT_INTERFACE_CTRL
LPNET_DVR_INPUT_INTERFACE_CTRL = POINTER(struct_tagNET_DVR_INPUT_INTERFACE_CTRL)
tagNET_DVR_INPUT_INTERFACE_CTRL = struct_tagNET_DVR_INPUT_INTERFACE_CTRL
