from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SINGLESCREENCFG(Structure):
    pass

_S(struct_tagNET_DVR_SINGLESCREENCFG, [
    ('byScreenSeq', BYTE),
    ('bySubSystemNum', BYTE),
    ('byDispNum', BYTE),
    ('byRes', BYTE * 9),
])

NET_DVR_SINGLESCREENCFG = struct_tagNET_DVR_SINGLESCREENCFG
LPNET_DVR_SINGLESCREENCFG = POINTER(struct_tagNET_DVR_SINGLESCREENCFG)
tagNET_DVR_SINGLESCREENCFG = struct_tagNET_DVR_SINGLESCREENCFG
