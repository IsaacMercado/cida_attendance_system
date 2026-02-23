from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HISTORICDATACFG(Structure):
    pass

_S(struct_tagNET_DVR_HISTORICDATACFG, [
    ('dwSize', DWORD),
    ('dwTotalNum', DWORD),
    ('byRes', BYTE * 16),
])

NET_DVR_HISTORICDATACFG = struct_tagNET_DVR_HISTORICDATACFG
LPNET_DVR_HISTORICDATACFG = POINTER(struct_tagNET_DVR_HISTORICDATACFG)
tagNET_DVR_HISTORICDATACFG = struct_tagNET_DVR_HISTORICDATACFG
