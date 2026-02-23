from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ENTRANCEDET_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ENTRANCEDET_CFG, [
    ('dwSize', DWORD),
    ('byOfflineDetEnable', BYTE),
    ('byDetCycle', BYTE),
    ('byDevCtrlCode', BYTE),
    ('byRes', BYTE * 61),
])

NET_DVR_ENTRANCEDET_CFG = struct_tagNET_DVR_ENTRANCEDET_CFG
LPNET_DVR_ENTRANCEDET_CFG = POINTER(struct_tagNET_DVR_ENTRANCEDET_CFG)
tagNET_DVR_ENTRANCEDET_CFG = struct_tagNET_DVR_ENTRANCEDET_CFG
