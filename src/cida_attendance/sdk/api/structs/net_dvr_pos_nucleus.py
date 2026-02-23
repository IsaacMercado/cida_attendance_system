from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POS_NUCLEUS(Structure):
    pass

_S(struct_tagNET_DVR_POS_NUCLEUS, [
    ('szEmployeeNo', c_char * 8),
    ('szTerminalNo', c_char * 8),
    ('szShiftNo', c_char * 8),
    ('byRes', BYTE * 928),
])

NET_DVR_POS_NUCLEUS = struct_tagNET_DVR_POS_NUCLEUS
LPNET_DVR_POS_NUCLEUS = POINTER(struct_tagNET_DVR_POS_NUCLEUS)
tagNET_DVR_POS_NUCLEUS = struct_tagNET_DVR_POS_NUCLEUS
