from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_deccard_ability_v41 import NET_DVR_DECCARD_ABILITY_V41


class struct_tagNET_DVR_DECODESVR_ABILITY_V41(Structure):
    pass

_S(struct_tagNET_DVR_DECODESVR_ABILITY_V41, [
    ('dwSize', DWORD),
    ('byCardNums', BYTE),
    ('byStartChan', BYTE),
    ('byRes1', BYTE * 2),
    ('struDecCardAbility', NET_DVR_DECCARD_ABILITY_V41 * 6),
    ('byRes2', BYTE * 64),
])

NET_DVR_DECODESVR_ABILITY_V41 = struct_tagNET_DVR_DECODESVR_ABILITY_V41
LPNET_DVR_DECODESVR_ABILITY_V41 = POINTER(struct_tagNET_DVR_DECODESVR_ABILITY_V41)
tagNET_DVR_DECODESVR_ABILITY_V41 = struct_tagNET_DVR_DECODESVR_ABILITY_V41
