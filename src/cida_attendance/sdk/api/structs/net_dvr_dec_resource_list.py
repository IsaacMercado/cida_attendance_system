from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEC_RESOURCE_LIST(Structure):
    pass

_S(struct_tagNET_DVR_DEC_RESOURCE_LIST, [
    ('dwSize', DWORD),
    ('byDecStatus', BYTE * 120),
    ('byRes', BYTE * 32),
])

NET_DVR_DEC_RESOURCE_LIST = struct_tagNET_DVR_DEC_RESOURCE_LIST
LPNET_DVR_DEC_RESOURCE_LIST = POINTER(struct_tagNET_DVR_DEC_RESOURCE_LIST)
tagNET_DVR_DEC_RESOURCE_LIST = struct_tagNET_DVR_DEC_RESOURCE_LIST
