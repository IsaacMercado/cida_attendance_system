from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INFRARED_OUTPUT_CTRL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_INFRARED_OUTPUT_CTRL_CFG, [
    ('dwSize', DWORD),
    ('byIROutPort', BYTE),
    ('byIRCmdIndex', BYTE),
    ('byRes', BYTE * 254),
])

NET_DVR_INFRARED_OUTPUT_CTRL_CFG = struct_tagNET_DVR_INFRARED_OUTPUT_CTRL_CFG
LPNET_DVR_INFRARED_OUTPUT_CTRL_CFG = POINTER(struct_tagNET_DVR_INFRARED_OUTPUT_CTRL_CFG)
tagNET_DVR_INFRARED_OUTPUT_CTRL_CFG = struct_tagNET_DVR_INFRARED_OUTPUT_CTRL_CFG
