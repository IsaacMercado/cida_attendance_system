from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_codecard_ability import NET_DVR_CODECARD_ABILITY


class struct_tagNET_DVR_CODESVR_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_CODESVR_ABILITY, [
    ('dwSize', DWORD),
    ('byCardNums', BYTE),
    ('byStartChan', BYTE),
    ('byRes1', BYTE * 2),
    ('struCodeCardAbility', NET_DVR_CODECARD_ABILITY * 8),
    ('byRes2', BYTE * 64),
])

NET_DVR_CODESVR_ABILITY = struct_tagNET_DVR_CODESVR_ABILITY
LPNET_DVR_CODESVR_ABILITY = POINTER(struct_tagNET_DVR_CODESVR_ABILITY)
tagNET_DVR_CODESVR_ABILITY = struct_tagNET_DVR_CODESVR_ABILITY
