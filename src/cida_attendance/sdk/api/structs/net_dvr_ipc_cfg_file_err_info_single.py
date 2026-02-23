from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IPC_CFG_FILE_ERR_INFO_SINGLE(Structure):
    pass

_S(struct_tagNET_DVR_IPC_CFG_FILE_ERR_INFO_SINGLE, [
    ('wRow', WORD),
    ('wErrCode', WORD),
    ('byRes', BYTE * 32),
])

NET_DVR_IPC_CFG_FILE_ERR_INFO_SINGLE = struct_tagNET_DVR_IPC_CFG_FILE_ERR_INFO_SINGLE
LPNET_DVR_IPC_CFG_FILE_ERR_INFO_SINGLE = POINTER(struct_tagNET_DVR_IPC_CFG_FILE_ERR_INFO_SINGLE)
tagNET_DVR_IPC_CFG_FILE_ERR_INFO_SINGLE = struct_tagNET_DVR_IPC_CFG_FILE_ERR_INFO_SINGLE
