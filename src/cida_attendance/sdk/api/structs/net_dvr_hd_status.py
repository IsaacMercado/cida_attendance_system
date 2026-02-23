from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HD_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_HD_STATUS, [
    ('dwSize', DWORD),
    ('bySleepStatus', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_HD_STATUS = struct_tagNET_DVR_HD_STATUS
LPNET_DVR_HD_STATUS = POINTER(struct_tagNET_DVR_HD_STATUS)
tagNET_DVR_HD_STATUS = struct_tagNET_DVR_HD_STATUS
