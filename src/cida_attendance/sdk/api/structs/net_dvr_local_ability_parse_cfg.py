from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_ABILITY_PARSE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_ABILITY_PARSE_CFG, [
    ('byEnableAbilityParse', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_LOCAL_ABILITY_PARSE_CFG = struct_tagNET_DVR_LOCAL_ABILITY_PARSE_CFG
LPNET_DVR_LOCAL_ABILITY_PARSE_CFG = POINTER(struct_tagNET_DVR_LOCAL_ABILITY_PARSE_CFG)
tagNET_DVR_LOCAL_ABILITY_PARSE_CFG = struct_tagNET_DVR_LOCAL_ABILITY_PARSE_CFG
