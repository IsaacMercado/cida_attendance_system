from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_GOP_INFO_PASSBACK(Structure):
    pass

_S(struct_tagNET_DVR_GOP_INFO_PASSBACK, [
    ('dwSize', DWORD),
    ('struTime', NET_DVR_TIME_V30),
    ('dwDuration', DWORD),
    ('dwMetaDataSize', DWORD),
    ('dwPicDataSize', DWORD),
    ('pMetaDataBuffer', String),
    ('pPicDataBuf', String),
    ('byRes', BYTE * 32),
])

NET_DVR_GOP_INFO_PASSBACK = struct_tagNET_DVR_GOP_INFO_PASSBACK
LPNET_DVR_GOP_INFO_PASSBACK = POINTER(struct_tagNET_DVR_GOP_INFO_PASSBACK)
tagNET_DVR_GOP_INFO_PASSBACK = struct_tagNET_DVR_GOP_INFO_PASSBACK
