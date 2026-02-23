from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_LIMITCFG(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_LIMITCFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byLimitStatus', BYTE),
    ('byRes', BYTE * 122),
])

NET_DVR_PTZ_LIMITCFG = struct_tagNET_DVR_PTZ_LIMITCFG
LPNET_DVR_PTZ_LIMITCFG = POINTER(struct_tagNET_DVR_PTZ_LIMITCFG)
tagNET_DVR_PTZ_LIMITCFG = struct_tagNET_DVR_PTZ_LIMITCFG
