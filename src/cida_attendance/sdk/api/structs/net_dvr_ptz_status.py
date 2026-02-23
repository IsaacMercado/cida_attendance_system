from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_STATUS, [
    ('dwSize', DWORD),
    ('dwUserID', DWORD),
    ('dwStatus', DWORD),
    ('dwRestTime', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_PTZ_STATUS = struct_tagNET_DVR_PTZ_STATUS
LPNET_DVR_PTZ_STATUS = POINTER(struct_tagNET_DVR_PTZ_STATUS)
tagNET_DVR_PTZ_STATUS = struct_tagNET_DVR_PTZ_STATUS
