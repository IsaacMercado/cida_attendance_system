from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_deccard_ability import NET_DVR_DECCARD_ABILITY


class struct_tagNET_DVR_DECODESVR_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_DECODESVR_ABILITY, [
    ('dwSize', DWORD),
    ('byCardNums', BYTE),
    ('byStartChan', BYTE),
    ('byRes1', BYTE * 2),
    ('struDecCardAbility', NET_DVR_DECCARD_ABILITY * 6),
    ('byRes2', BYTE * 64),
])

NET_DVR_DECODESVR_ABILITY = struct_tagNET_DVR_DECODESVR_ABILITY
LPNET_DVR_DECODESVR_ABILITY = POINTER(struct_tagNET_DVR_DECODESVR_ABILITY)
tagNET_DVR_DECODESVR_ABILITY = struct_tagNET_DVR_DECODESVR_ABILITY
