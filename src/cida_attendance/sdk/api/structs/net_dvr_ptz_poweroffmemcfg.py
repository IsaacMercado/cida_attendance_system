from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_POWEROFFMEMCFG(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_POWEROFFMEMCFG, [
    ('dwSize', DWORD),
    ('byResumeTimePoint', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_PTZ_POWEROFFMEMCFG = struct_tagNET_DVR_PTZ_POWEROFFMEMCFG
LPNET_DVR_PTZ_POWEROFFMEMCFG = POINTER(struct_tagNET_DVR_PTZ_POWEROFFMEMCFG)
tagNET_DVR_PTZ_POWEROFFMEMCFG = struct_tagNET_DVR_PTZ_POWEROFFMEMCFG
