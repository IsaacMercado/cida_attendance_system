from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_vd_slot import NET_DVR_VD_SLOT


class struct_tagNET_DVR_ARRAY_SPACE_ALLOC_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ARRAY_SPACE_ALLOC_INFO, [
    ('byVDSlotCount', BYTE),
    ('byRes1', BYTE * 3),
    ('struVDSlots', NET_DVR_VD_SLOT * 128),
])

NET_DVR_ARRAY_SPACE_ALLOC_INFO = struct_tagNET_DVR_ARRAY_SPACE_ALLOC_INFO
LPNET_DVR_ARRAY_SPACE_ALLOC_INFO = POINTER(struct_tagNET_DVR_ARRAY_SPACE_ALLOC_INFO)
tagNET_DVR_ARRAY_SPACE_ALLOC_INFO = struct_tagNET_DVR_ARRAY_SPACE_ALLOC_INFO
