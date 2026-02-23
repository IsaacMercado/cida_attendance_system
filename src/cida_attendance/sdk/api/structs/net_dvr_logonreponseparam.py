from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOGONREPONSEPARAM(Structure):
    pass

_S(struct_tagNET_DVR_LOGONREPONSEPARAM, [
    ('wHeartbeatTime', WORD),
    ('byOvertimes', BYTE),
    ('byRes', BYTE * 13),
])

NET_DVR_LOGONREPONSEPARAM = struct_tagNET_DVR_LOGONREPONSEPARAM
LPNET_DVR_LOGONREPONSEPARAM = POINTER(struct_tagNET_DVR_LOGONREPONSEPARAM)
tagNET_DVR_LOGONREPONSEPARAM = struct_tagNET_DVR_LOGONREPONSEPARAM
