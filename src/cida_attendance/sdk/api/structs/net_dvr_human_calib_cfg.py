from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_HUMAN_CALIB_CFG(Structure):
    pass

_S(struct_tagNET_DVR_HUMAN_CALIB_CFG, [
    ('dwSize', DWORD),
    ('struLeftPos', NET_VCA_POINT),
    ('struRightPos', NET_VCA_POINT),
    ('byRes', BYTE * 300),
])

NET_DVR_HUMAN_CALIB_CFG = struct_tagNET_DVR_HUMAN_CALIB_CFG
LPNET_DVR_HUMAN_CALIB_CFG = POINTER(struct_tagNET_DVR_HUMAN_CALIB_CFG)
tagNET_DVR_HUMAN_CALIB_CFG = struct_tagNET_DVR_HUMAN_CALIB_CFG
