from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_frame import NET_DVR_FRAME


class struct_tagNET_DVR_FRAME_CFG(Structure):
    pass

_S(struct_tagNET_DVR_FRAME_CFG, [
    ('dwSize', DWORD),
    ('struTopFrame', NET_DVR_FRAME),
    ('struBottomFrame', NET_DVR_FRAME),
    ('struLeftFrame', NET_DVR_FRAME),
    ('struRightFrame', NET_DVR_FRAME),
    ('byFrameEnable', BYTE),
    ('byRes', BYTE * 256),
])

NET_DVR_FRAME_CFG = struct_tagNET_DVR_FRAME_CFG
LPNET_DVR_FRAME_CFG = POINTER(struct_tagNET_DVR_FRAME_CFG)
tagNET_DVR_FRAME_CFG = struct_tagNET_DVR_FRAME_CFG
