from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from ..enums import INIT_CFG_MAX_NUM


class struct_tagNET_DVR_INIT_CFG_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_INIT_CFG_ABILITY, [
    ('enumMaxLoginUsersNum', INIT_CFG_MAX_NUM),
    ('enumMaxAlarmNum', INIT_CFG_MAX_NUM),
    ('byRes', BYTE * 64),
])

NET_DVR_INIT_CFG_ABILITY = struct_tagNET_DVR_INIT_CFG_ABILITY
LPNET_DVR_INIT_CFG_ABILITY = POINTER(struct_tagNET_DVR_INIT_CFG_ABILITY)
tagNET_DVR_INIT_CFG_ABILITY = struct_tagNET_DVR_INIT_CFG_ABILITY
