from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_lockgate_time_cfg import NET_DVR_LOCKGATE_TIME_CFG


class struct_tagNET_DVR_LOCKGATE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LOCKGATE_CFG, [
    ('dwSize', DWORD),
    ('struTime', NET_DVR_LOCKGATE_TIME_CFG * 4),
    ('byRes', BYTE * 128),
])

NET_DVR_LOCKGATE_CFG = struct_tagNET_DVR_LOCKGATE_CFG
LPNET_DVR_LOCKGATE_CFG = POINTER(struct_tagNET_DVR_LOCKGATE_CFG)
tagNET_DVR_LOCKGATE_CFG = struct_tagNET_DVR_LOCKGATE_CFG
