from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_DVR_OUTPUT_OSD_CFG(Structure):
    pass

_S(struct_tagNET_DVR_OUTPUT_OSD_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byFontSize', BYTE),
    ('byOSDColor', BYTE),
    ('byRes1', BYTE * 1),
    ('byOsdContent', BYTE * 64),
    ('struRect', NET_DVR_RECTCFG_EX),
    ('dwOsdWinNo', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_OUTPUT_OSD_CFG = struct_tagNET_DVR_OUTPUT_OSD_CFG
LPNET_DVR_OUTPUT_OSD_CFG = POINTER(struct_tagNET_DVR_OUTPUT_OSD_CFG)
tagNET_DVR_OUTPUT_OSD_CFG = struct_tagNET_DVR_OUTPUT_OSD_CFG
