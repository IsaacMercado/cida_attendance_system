from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MB_PLATFORM_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_MB_PLATFORM_STATUS, [
    ('byCurPlat', BYTE),
    ('byLoginStatus', BYTE),
    ('byExceptionInfo', BYTE),
    ('byres', BYTE * 5),
])

NET_DVR_MB_PLATFORM_STATUS = struct_tagNET_DVR_MB_PLATFORM_STATUS
LPNET_DVR_MB_PLATFORM_STATUS = POINTER(struct_tagNET_DVR_MB_PLATFORM_STATUS)
tagNET_DVR_MB_PLATFORM_STATUS = struct_tagNET_DVR_MB_PLATFORM_STATUS
