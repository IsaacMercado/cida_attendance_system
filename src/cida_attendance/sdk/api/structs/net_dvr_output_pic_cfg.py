from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_DVR_OUTPUT_PIC_CFG(Structure):
    pass

_S(struct_tagNET_DVR_OUTPUT_PIC_CFG, [
    ('dwSize', DWORD),
    ('dwOutputPicNo', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struRect', NET_DVR_RECTCFG_EX),
    ('byFlash', BYTE),
    ('byTranslucent', BYTE),
    ('byRes2', BYTE * 2),
    ('dwOutputPicWinNo', DWORD),
    ('byRes3', BYTE * 28),
])

NET_DVR_OUTPUT_PIC_CFG = struct_tagNET_DVR_OUTPUT_PIC_CFG
LPNET_DVR_OUTPUT_PIC_CFG = POINTER(struct_tagNET_DVR_OUTPUT_PIC_CFG)
tagNET_DVR_OUTPUT_PIC_CFG = struct_tagNET_DVR_OUTPUT_PIC_CFG
