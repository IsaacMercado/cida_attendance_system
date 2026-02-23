from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ACCELERATIONCFG(Structure):
    pass

_S(struct_tagNET_DVR_ACCELERATIONCFG, [
    ('dwMaxXAcc', DWORD),
    ('dwMaxYAcc', DWORD),
    ('dwMaxZAcc', DWORD),
    ('byRes', BYTE * 4),
])

NET_DVR_ACCELERATIONCFG = struct_tagNET_DVR_ACCELERATIONCFG
LPNET_DVR_ACCERATIONCFG = POINTER(struct_tagNET_DVR_ACCELERATIONCFG)
tagNET_DVR_ACCELERATIONCFG = struct_tagNET_DVR_ACCELERATIONCFG
