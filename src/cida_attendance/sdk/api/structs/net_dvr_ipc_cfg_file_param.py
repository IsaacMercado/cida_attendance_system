from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IPC_CFG_FILE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_IPC_CFG_FILE_PARAM, [
    ('szFileName', c_char * 260),
    ('byRes', BYTE * 32),
])

NET_DVR_IPC_CFG_FILE_PARAM = struct_tagNET_DVR_IPC_CFG_FILE_PARAM
LPNET_DVR_IPC_CFG_FILE_PARAM = POINTER(struct_tagNET_DVR_IPC_CFG_FILE_PARAM)
tagNET_DVR_IPC_CFG_FILE_PARAM = struct_tagNET_DVR_IPC_CFG_FILE_PARAM
