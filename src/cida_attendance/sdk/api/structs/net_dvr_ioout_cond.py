from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IOOUT_COND(Structure):
    pass

_S(struct_tagNET_DVR_IOOUT_COND, [
    ('dwSize', DWORD),
    ('bySyncOutputNo', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_IOOUT_COND = struct_tagNET_DVR_IOOUT_COND
LPNET_DVR_IOOUT_COND = POINTER(struct_tagNET_DVR_IOOUT_COND)
tagNET_DVR_IOOUT_COND = struct_tagNET_DVR_IOOUT_COND
