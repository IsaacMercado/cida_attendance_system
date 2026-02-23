from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FORM_DATA_CFG(Structure):
    pass

_S(struct_tagNET_DVR_FORM_DATA_CFG, [
    ('dwSize', DWORD),
    ('lpBuffer', POINTER(None)),
    ('dwBufferSize', DWORD),
    ('byNumOfMultiPart', BYTE),
    ('byRes', BYTE * 67),
])

NET_DVR_FORM_DATA_CFG = struct_tagNET_DVR_FORM_DATA_CFG
LPNET_DVR_FORM_DATA_CFG = POINTER(struct_tagNET_DVR_FORM_DATA_CFG)
tagNET_DVR_FORM_DATA_CFG = struct_tagNET_DVR_FORM_DATA_CFG
