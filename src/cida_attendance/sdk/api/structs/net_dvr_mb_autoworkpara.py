from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_MB_AUTOWORKPARA(Structure):
    pass

_S(struct_tagNET_DVR_MB_AUTOWORKPARA, [
    ('byCurPowerCtrlType', BYTE),
    ('byRes', BYTE * 3),
    ('struWorkTime', (NET_DVR_SCHEDTIME * 2) * 7),
])

NET_DVR_MB_AUTOWORKPARA = struct_tagNET_DVR_MB_AUTOWORKPARA
LPNET_DVR_MB_AUTOWORKPARA = POINTER(struct_tagNET_DVR_MB_AUTOWORKPARA)
tagNET_DVR_MB_AUTOWORKPARA = struct_tagNET_DVR_MB_AUTOWORKPARA
