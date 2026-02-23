from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from ..functions import LOGCALLBACK


class struct_tagNET_DVR_LOCAL_LOG_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_LOG_CFG, [
    ('wSDKLogNum', WORD),
    ('fnCB', LOGCALLBACK),
    ('pUserData', POINTER(None)),
    ('byRes', BYTE * 238),
])

NET_DVR_LOCAL_LOG_CFG = struct_tagNET_DVR_LOCAL_LOG_CFG
LPNET_DVR_LOCAL_LOG_CFG = POINTER(struct_tagNET_DVR_LOCAL_LOG_CFG)
tagNET_DVR_LOCAL_LOG_CFG = struct_tagNET_DVR_LOCAL_LOG_CFG
