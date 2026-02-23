from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30
from .net_dvr_accelerationcfg import NET_DVR_ACCELERATIONCFG


class struct_tagNET_DVR_GSENSORPARA(Structure):
    pass

_S(struct_tagNET_DVR_GSENSORPARA, [
    ('dwSize', DWORD),
    ('struAccelerationCfg', NET_DVR_ACCELERATIONCFG),
    ('byModuleSelect', BYTE),
    ('byRes1', BYTE * 3),
    ('struHandleException', NET_DVR_HANDLEEXCEPTION_V30),
    ('byRes2', BYTE * 24),
])

NET_DVR_GSENSORPARA = struct_tagNET_DVR_GSENSORPARA
LPNET_DVR_GSENSORPARA = POINTER(struct_tagNET_DVR_GSENSORPARA)
tagNET_DVR_GSENSORPARA = struct_tagNET_DVR_GSENSORPARA
