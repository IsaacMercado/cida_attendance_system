from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SNAPINFO_COND_(Structure):
    pass

_S(struct_tagNET_DVR_SNAPINFO_COND_, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('byRelateType', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_SNAPINFO_COND = struct_tagNET_DVR_SNAPINFO_COND_
LPNET_DVR_SNAPINFO_COND = POINTER(struct_tagNET_DVR_SNAPINFO_COND_)
tagNET_DVR_SNAPINFO_COND_ = struct_tagNET_DVR_SNAPINFO_COND_
