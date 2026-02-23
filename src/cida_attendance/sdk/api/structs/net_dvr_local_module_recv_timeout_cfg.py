from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_MODULE_RECV_TIMEOUT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_MODULE_RECV_TIMEOUT_CFG, [
    ('dwPreviewTime', DWORD),
    ('dwAlarmTime', DWORD),
    ('dwVodTime', DWORD),
    ('dwElse', DWORD),
    ('byRes', BYTE * 512),
])

NET_DVR_LOCAL_MODULE_RECV_TIMEOUT_CFG = struct_tagNET_DVR_LOCAL_MODULE_RECV_TIMEOUT_CFG
LPNET_DVR_LOCAL_MODULE_RECV_TIMEOUT_CFG = POINTER(struct_tagNET_DVR_LOCAL_MODULE_RECV_TIMEOUT_CFG)
tagNET_DVR_LOCAL_MODULE_RECV_TIMEOUT_CFG = struct_tagNET_DVR_LOCAL_MODULE_RECV_TIMEOUT_CFG
