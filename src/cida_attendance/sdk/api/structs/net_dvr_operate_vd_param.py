from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OPERATE_VD_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_OPERATE_VD_PARAM, [
    ('wArrayID', WORD),
    ('bySlot', BYTE),
    ('byInitType', BYTE),
    ('dwHCapacity', DWORD),
    ('dwLCapacity', DWORD),
    ('byName', BYTE * 16),
    ('byRes2', BYTE * 16),
])

NET_DVR_OPERATE_VD_PARAM = struct_tagNET_DVR_OPERATE_VD_PARAM
LPNET_DVR_OPERATE_VD_PARAM = POINTER(struct_tagNET_DVR_OPERATE_VD_PARAM)
tagNET_DVR_OPERATE_VD_PARAM = struct_tagNET_DVR_OPERATE_VD_PARAM
