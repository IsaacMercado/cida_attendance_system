from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_ability_list import NET_DVR_ABILITY_LIST


class struct_tagNET_DVR_COMPRESSIONCFG_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_COMPRESSIONCFG_ABILITY, [
    ('dwSize', DWORD),
    ('dwAbilityNum', DWORD),
    ('struAbilityNode', NET_DVR_ABILITY_LIST * 12),
])

NET_DVR_COMPRESSIONCFG_ABILITY = struct_tagNET_DVR_COMPRESSIONCFG_ABILITY
LPNET_DVR_COMPRESSIONCFG_ABILITY = POINTER(struct_tagNET_DVR_COMPRESSIONCFG_ABILITY)
tagNET_DVR_COMPRESSIONCFG_ABILITY = struct_tagNET_DVR_COMPRESSIONCFG_ABILITY
