from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_associatecfg import NET_DVR_ASSOCIATECFG
from .net_dvr_pu_stream_cfg import NET_DVR_PU_STREAM_CFG


class struct_tagNET_DVR_DYNAMICDECODE(Structure):
    pass

_S(struct_tagNET_DVR_DYNAMICDECODE, [
    ('dwSize', DWORD),
    ('struAssociateCfg', NET_DVR_ASSOCIATECFG),
    ('struPuStreamCfg', NET_DVR_PU_STREAM_CFG),
    ('byRes', BYTE * 8),
])

NET_DVR_DYNAMICDECODE = struct_tagNET_DVR_DYNAMICDECODE
LPNET_DVR_DYNAMICDECODE = POINTER(struct_tagNET_DVR_DYNAMICDECODE)
tagNET_DVR_DYNAMICDECODE = struct_tagNET_DVR_DYNAMICDECODE
