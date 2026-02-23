from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INFRARED_CMD_INFO(Structure):
    pass

_S(struct_tagNET_DVR_INFRARED_CMD_INFO, [
    ('sCmdName', c_char * 32),
    ('byRes', BYTE * 8),
])

NET_DVR_INFRARED_CMD_INFO = struct_tagNET_DVR_INFRARED_CMD_INFO
LPNET_DVR_INFRARED_CMD_INFO = POINTER(struct_tagNET_DVR_INFRARED_CMD_INFO)
tagNET_DVR_INFRARED_CMD_INFO = struct_tagNET_DVR_INFRARED_CMD_INFO
