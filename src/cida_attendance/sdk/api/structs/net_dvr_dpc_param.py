from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_DPC_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_DPC_PARAM, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('wCtrlType', WORD),
    ('byDPCMode', BYTE),
    ('byRes', BYTE),
    ('struPoint', NET_VCA_POINT),
    ('byRes1', BYTE * 64),
])

NET_DVR_DPC_PARAM = struct_tagNET_DVR_DPC_PARAM
LPNET_DVR_DPC_PARAM = POINTER(struct_tagNET_DVR_DPC_PARAM)
tagNET_DVR_DPC_PARAM = struct_tagNET_DVR_DPC_PARAM
