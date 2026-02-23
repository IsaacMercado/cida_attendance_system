from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_desc_node import NET_DVR_DESC_NODE


class struct_tagNET_DVR_ABILITY_LIST(Structure):
    pass

_S(struct_tagNET_DVR_ABILITY_LIST, [
    ('dwAbilityType', DWORD),
    ('byRes', BYTE * 32),
    ('dwNodeNum', DWORD),
    ('struDescNode', NET_DVR_DESC_NODE * 256),
])

NET_DVR_ABILITY_LIST = struct_tagNET_DVR_ABILITY_LIST
LPNET_DVR_ABILITY_LIST = POINTER(struct_tagNET_DVR_ABILITY_LIST)
tagNET_DVR_ABILITY_LIST = struct_tagNET_DVR_ABILITY_LIST
