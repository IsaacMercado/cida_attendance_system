from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SDKLOCAL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SDKLOCAL_CFG, [
    ('byEnableAbilityParse', BYTE),
    ('byVoiceComMode', BYTE),
    ('byLoginWithSimXml', BYTE),
    ('byCompatibleType', BYTE),
    ('byRes', BYTE * 380),
    ('byProtectKey', BYTE * 128),
])

NET_DVR_SDKLOCAL_CFG = struct_tagNET_DVR_SDKLOCAL_CFG
LPNET_DVR_SDKLOCAL_CFG = POINTER(struct_tagNET_DVR_SDKLOCAL_CFG)
tagNET_DVR_SDKLOCAL_CFG = struct_tagNET_DVR_SDKLOCAL_CFG
