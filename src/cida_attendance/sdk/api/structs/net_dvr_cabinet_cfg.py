from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_cabinet_alarm_paramcfg import NET_DVR_CABINET_AlARM_PARAMCFG


class struct_tagNET_DVR_CABINET_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CABINET_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 3),
    ('struCabinetCfg', NET_DVR_CABINET_AlARM_PARAMCFG * 8),
    ('byRes1', BYTE * 84),
])

NET_DVR_CABINET_CFG = struct_tagNET_DVR_CABINET_CFG
LPNET_DVR_CABINET_CFG = POINTER(struct_tagNET_DVR_CABINET_CFG)
tagNET_DVR_CABINET_CFG = struct_tagNET_DVR_CABINET_CFG
