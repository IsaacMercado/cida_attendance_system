from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_GOP_INFO_RET(Structure):
    pass

_S(struct_tagNET_DVR_GOP_INFO_RET, [
    ('struGopTime', NET_DVR_TIME_V30),
    ('dwDuration', DWORD),
    ('dwDataSize', DWORD),
    ('byRes', BYTE * 128),
    ('pBuf', String),
])

NET_DVR_GOP_INFO_RET = struct_tagNET_DVR_GOP_INFO_RET
LPNET_DVR_GOP_INFO_RET = POINTER(struct_tagNET_DVR_GOP_INFO_RET)
tagNET_DVR_GOP_INFO_RET = struct_tagNET_DVR_GOP_INFO_RET
