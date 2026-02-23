from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CALLBACK_TYPE_DATA(Structure):
    pass

_S(struct_tagNET_DVR_CALLBACK_TYPE_DATA, [
    ('dwChannel', DWORD),
    ('dwDataType', DWORD),
    ('dwDataLen', DWORD),
    ('pData', POINTER(BYTE)),
    ('byRes', BYTE * 64),
])

NET_DVR_CALLBACK_TYPE_DATA = struct_tagNET_DVR_CALLBACK_TYPE_DATA
LPNET_DVR_CALLBACK_TYPE_DATA = POINTER(struct_tagNET_DVR_CALLBACK_TYPE_DATA)
tagNET_DVR_CALLBACK_TYPE_DATA = struct_tagNET_DVR_CALLBACK_TYPE_DATA
