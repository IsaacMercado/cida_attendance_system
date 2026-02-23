from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_pppdparam import NET_DVR_PPPDPARAM
from .net_dvr_qosparam import NET_DVR_QOSPARAM


class struct_tagNET_DVR_DIALPARAM(Structure):
    pass

_S(struct_tagNET_DVR_DIALPARAM, [
    ('dwSize', DWORD),
    ('bEnable3G', BYTE),
    ('byDialMethod', BYTE),
    ('bySwitchMethod', BYTE),
    ('byEnaAlarmInDial', BYTE),
    ('byRes1', BYTE * 10),
    ('wOffLineTime', WORD),
    ('struPppdParam', NET_DVR_PPPDPARAM),
    ('struQosParam', NET_DVR_QOSPARAM),
    ('byUimNumber', BYTE * 32),
    ('byRes2', BYTE * 24),
])

NET_DVR_DIALPARAM = struct_tagNET_DVR_DIALPARAM
LPNET_DVR_DIALPARAM = POINTER(struct_tagNET_DVR_DIALPARAM)
tagNET_DVR_DIALPARAM = struct_tagNET_DVR_DIALPARAM
