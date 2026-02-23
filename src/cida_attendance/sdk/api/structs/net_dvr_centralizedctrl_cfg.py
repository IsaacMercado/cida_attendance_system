from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_lli_param import NET_DVR_LLI_PARAM


class struct_tagNET_DVR_CENTRALIZEDCTRL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CENTRALIZEDCTRL_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byLatitudeType', BYTE),
    ('byLongitudeType', BYTE),
    ('byRes1', BYTE),
    ('struLatitude', NET_DVR_LLI_PARAM),
    ('struLongitude', NET_DVR_LLI_PARAM),
    ('dwTimeOut', DWORD),
    ('byControlType', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_CENTRALIZEDCTRL_CFG = struct_tagNET_DVR_CENTRALIZEDCTRL_CFG
LPNET_DVR_CENTRALIZEDCTRL_CFG = POINTER(struct_tagNET_DVR_CENTRALIZEDCTRL_CFG)
tagNET_DVR_CENTRALIZEDCTRL_CFG = struct_tagNET_DVR_CENTRALIZEDCTRL_CFG
