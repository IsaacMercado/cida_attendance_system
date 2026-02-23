from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INFRARED_LEARN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_INFRARED_LEARN_INFO, [
    ('dwSize', DWORD),
    ('byIROutPort', BYTE),
    ('byIRCmdIndex', BYTE),
    ('byRes', BYTE * 30),
])

NET_DVR_INFRARED_LEARN_INFO = struct_tagNET_DVR_INFRARED_LEARN_INFO
LPNET_DVR_INFRARED_LEARN_INFO = POINTER(struct_tagNET_DVR_INFRARED_LEARN_INFO)
tagNET_DVR_INFRARED_LEARN_INFO = struct_tagNET_DVR_INFRARED_LEARN_INFO
