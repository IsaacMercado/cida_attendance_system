from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_DVR_MSC_SPLICE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MSC_SPLICE_CFG, [
    ('dwSize', DWORD),
    ('bySpliceNo', BYTE),
    ('byWallNo', BYTE),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 1),
    ('struRectCfg', NET_DVR_RECTCFG_EX),
    ('byRes2', BYTE * 32),
])

NET_DVR_MSC_SPLICE_CFG = struct_tagNET_DVR_MSC_SPLICE_CFG
LPNET_DVR_MSC_SPLICE_CFG = POINTER(struct_tagNET_DVR_MSC_SPLICE_CFG)
tagNET_DVR_MSC_SPLICE_CFG = struct_tagNET_DVR_MSC_SPLICE_CFG
