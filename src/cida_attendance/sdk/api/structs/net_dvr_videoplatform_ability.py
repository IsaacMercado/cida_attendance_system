from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_subsystem_ability import NET_DVR_SUBSYSTEM_ABILITY


class struct_tagNET_DVR_VIDEOPLATFORM_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_VIDEOPLATFORM_ABILITY, [
    ('dwSize', DWORD),
    ('byCodeSubSystemNums', BYTE),
    ('byDecodeSubSystemNums', BYTE),
    ('bySupportNat', BYTE),
    ('byRes1', BYTE * 17),
    ('struSubSystemAbility', NET_DVR_SUBSYSTEM_ABILITY * 80),
    ('byRes2', BYTE * 640),
])

NET_DVR_VIDEOPLATFORM_ABILITY = struct_tagNET_DVR_VIDEOPLATFORM_ABILITY
LPNET_DVR_VIDEOPLATFORM_ABILITY = POINTER(struct_tagNET_DVR_VIDEOPLATFORM_ABILITY)
tagNET_DVR_VIDEOPLATFORM_ABILITY = struct_tagNET_DVR_VIDEOPLATFORM_ABILITY
