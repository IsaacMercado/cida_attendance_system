from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SDI_INFO(Structure):
    pass

_S(struct_tagNET_DVR_SDI_INFO, [
    ('byChanNums', BYTE),
    ('byStartChan', BYTE),
    ('byRes', BYTE * 2),
    ('dwSupportResolution', DWORD * 16),
])

NET_DVR_SDI_INFO = struct_tagNET_DVR_SDI_INFO
LPNET_DVR_SDI_INFO = POINTER(struct_tagNET_DVR_SDI_INFO)
tagNET_DVR_SDI_INFO = struct_tagNET_DVR_SDI_INFO
