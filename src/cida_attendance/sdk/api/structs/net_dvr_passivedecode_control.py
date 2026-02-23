from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PASSIVEDECODE_CONTROL(Structure):
    pass

_S(struct_tagNET_DVR_PASSIVEDECODE_CONTROL, [
    ('dwSize', DWORD),
    ('dwPlayCmd', DWORD),
    ('dwCmdParam', DWORD),
    ('byRes', BYTE * 16),
])

NET_DVR_PASSIVEDECODE_CONTROL = struct_tagNET_DVR_PASSIVEDECODE_CONTROL
LPNET_DVR_PASSIVEDECODE_CONTROL = POINTER(struct_tagNET_DVR_PASSIVEDECODE_CONTROL)
tagNET_DVR_PASSIVEDECODE_CONTROL = struct_tagNET_DVR_PASSIVEDECODE_CONTROL
