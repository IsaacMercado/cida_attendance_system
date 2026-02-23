from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_npo_param_union import NET_DVR_NPO_PARAM_UNION


class struct_tagNET_DVR_N_PLUS_ONE_DEVICE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_N_PLUS_ONE_DEVICE_PARAM, [
    ('dwSize', DWORD),
    ('unionParam', NET_DVR_NPO_PARAM_UNION),
    ('byType', BYTE),
    ('byRes', BYTE * 3),
    ('szUserName', c_char * 32),
    ('byRes2', BYTE * 220),
])

NET_DVR_N_PLUS_ONE_DEVICE_PARAM = struct_tagNET_DVR_N_PLUS_ONE_DEVICE_PARAM
LPNET_DVR_N_PLUS_ONE_DEVICE_PARAM = POINTER(struct_tagNET_DVR_N_PLUS_ONE_DEVICE_PARAM)
tagNET_DVR_N_PLUS_ONE_DEVICE_PARAM = struct_tagNET_DVR_N_PLUS_ONE_DEVICE_PARAM
