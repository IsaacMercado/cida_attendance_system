from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_CHECK_DEV(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_CHECK_DEV, [
    ('dwCheckOnlineTimeout', DWORD),
    ('dwCheckOnlineNetFailMax', DWORD),
    ('byRes', BYTE * 256),
])

NET_DVR_LOCAL_CHECK_DEV = struct_tagNET_DVR_LOCAL_CHECK_DEV
LPNET_DVR_LOCAL_CHECK_DEV = POINTER(struct_tagNET_DVR_LOCAL_CHECK_DEV)
tagNET_DVR_LOCAL_CHECK_DEV = struct_tagNET_DVR_LOCAL_CHECK_DEV
