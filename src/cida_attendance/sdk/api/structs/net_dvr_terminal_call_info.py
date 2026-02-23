from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TERMINAL_CALL_INFO(Structure):
    pass

_S(struct_tagNET_DVR_TERMINAL_CALL_INFO, [
    ('byTermianlURL', BYTE * 512),
    ('dwCallRate', DWORD),
    ('byRes', BYTE * 124),
])

NET_DVR_TERMINAL_CALL_INFO = struct_tagNET_DVR_TERMINAL_CALL_INFO
LPNET_DVR_TERMINAL_CALL_INFO = POINTER(struct_tagNET_DVR_TERMINAL_CALL_INFO)
tagNET_DVR_TERMINAL_CALL_INFO = struct_tagNET_DVR_TERMINAL_CALL_INFO
