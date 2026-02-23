from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_SMSPARAM(Structure):
    pass

_S(struct_tagNET_DVR_SMSPARAM, [
    ('dwIndex', DWORD),
    ('byStatus', BYTE),
    ('byRes', BYTE * 7),
    ('struRecvTime', NET_DVR_TIME_EX),
])

NET_DVR_SMSPARAM = struct_tagNET_DVR_SMSPARAM
LPNET_DVR_SMSPARAM = POINTER(struct_tagNET_DVR_SMSPARAM)
tagNET_DVR_SMSPARAM = struct_tagNET_DVR_SMSPARAM
