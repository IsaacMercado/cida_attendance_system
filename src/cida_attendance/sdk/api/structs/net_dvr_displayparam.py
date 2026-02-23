from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DISPLAYPARAM(Structure):
    pass

_S(struct_tagNET_DVR_DISPLAYPARAM, [
    ('dwDisplayNo', DWORD),
    ('byDispChanType', BYTE),
    ('byRes', BYTE * 11),
])

NET_DVR_DISPLAYPARAM = struct_tagNET_DVR_DISPLAYPARAM
LPNET_DVR_DISPLAYPARAM = POINTER(struct_tagNET_DVR_DISPLAYPARAM)
tagNET_DVR_DISPLAYPARAM = struct_tagNET_DVR_DISPLAYPARAM
