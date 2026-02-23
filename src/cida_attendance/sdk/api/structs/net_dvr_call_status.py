from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CALL_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_CALL_STATUS, [
    ('dwSize', DWORD),
    ('byCallStatus', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_CALL_STATUS = struct_tagNET_DVR_CALL_STATUS
LPNET_DVR_CALL_STATUS = POINTER(struct_tagNET_DVR_CALL_STATUS)
tagNET_DVR_CALL_STATUS = struct_tagNET_DVR_CALL_STATUS
