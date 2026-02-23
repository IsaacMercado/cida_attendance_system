from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IO_INCFG(Structure):
    pass

_S(struct_tagNET_DVR_IO_INCFG, [
    ('dwSize', DWORD),
    ('byIoInStatus', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_IO_INCFG = struct_tagNET_DVR_IO_INCFG
LPNET_DVR_IO_INCFG = POINTER(struct_tagNET_DVR_IO_INCFG)
tagNET_DVR_IO_INCFG = struct_tagNET_DVR_IO_INCFG
