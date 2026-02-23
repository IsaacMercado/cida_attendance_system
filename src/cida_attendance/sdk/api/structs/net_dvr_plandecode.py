from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_decodesched import NET_DVR_DECODESCHED


class struct_tagNET_DVR_PLANDECODE(Structure):
    pass

_S(struct_tagNET_DVR_PLANDECODE, [
    ('dwSize', DWORD),
    ('struDecodeSched', (NET_DVR_DECODESCHED * 4) * 7),
    ('byRes', BYTE * 8),
])

NET_DVR_PLANDECODE = struct_tagNET_DVR_PLANDECODE
LPNET_DVR_PLANDECODE = POINTER(struct_tagNET_DVR_PLANDECODE)
tagNET_DVR_PLANDECODE = struct_tagNET_DVR_PLANDECODE
