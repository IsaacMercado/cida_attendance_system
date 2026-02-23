from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_SUBSERVERINFO(Structure):
    pass

_S(struct_tagNET_DVR_SUBSERVERINFO, [
    ('bySequence', BYTE),
    ('byBelongSubDomain', BYTE),
    ('byRes1', BYTE * 6),
    ('dwMaxIpcNums', DWORD),
    ('struSubMatrixIP', NET_DVR_IPADDR),
    ('wSubMatrixPort', WORD),
    ('byRes2', BYTE * 6),
])

NET_DVR_SUBSERVERINFO = struct_tagNET_DVR_SUBSERVERINFO
LPNET_DVR_SUBSERVERINFO = POINTER(struct_tagNET_DVR_SUBSERVERINFO)
tagNET_DVR_SUBSERVERINFO = struct_tagNET_DVR_SUBSERVERINFO
