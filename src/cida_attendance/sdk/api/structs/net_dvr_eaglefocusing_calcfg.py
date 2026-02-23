from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_eaglefocusing_sence import NET_DVR_EAGLEFOCUSING_SENCE


class struct_tagNET_DVR_EAGLEFOCUSING_CALCFG(Structure):
    pass

_S(struct_tagNET_DVR_EAGLEFOCUSING_CALCFG, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byRes1', BYTE * 3),
    ('struEagleFoucsing', NET_DVR_EAGLEFOCUSING_SENCE * 16),
    ('byRes', BYTE * 512),
])

NET_DVR_EAGLEFOCUSING_CALCFG = struct_tagNET_DVR_EAGLEFOCUSING_CALCFG
LPNET_DVR_EAGLEFOCUSING_CALCFG = POINTER(struct_tagNET_DVR_EAGLEFOCUSING_CALCFG)
tagNET_DVR_EAGLEFOCUSING_CALCFG = struct_tagNET_DVR_EAGLEFOCUSING_CALCFG
