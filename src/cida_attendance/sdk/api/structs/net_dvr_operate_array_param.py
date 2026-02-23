from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OPERATE_ARRAY_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_OPERATE_ARRAY_PARAM, [
    ('byRaidMode', BYTE),
    ('byPDCount', BYTE),
    ('wArrayID', WORD),
    ('wPDSlots', WORD * 16),
    ('byName', BYTE * 16),
    ('byInitMode', BYTE),
    ('byRes1', BYTE),
    ('wPDSlotsPartTwo', WORD * 8),
    ('byRes2', BYTE * 2),
])

NET_DVR_OPERATE_ARRAY_PARAM = struct_tagNET_DVR_OPERATE_ARRAY_PARAM
LPNET_DVR_OPERATE_ARRAY_PARAM = POINTER(struct_tagNET_DVR_OPERATE_ARRAY_PARAM)
tagNET_DVR_OPERATE_ARRAY_PARAM = struct_tagNET_DVR_OPERATE_ARRAY_PARAM
