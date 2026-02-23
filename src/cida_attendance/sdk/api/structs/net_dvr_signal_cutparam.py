from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SIGNAL_CUTPARAM(Structure):
    pass

_S(struct_tagNET_DVR_SIGNAL_CUTPARAM, [
    ('dwSize', DWORD),
    ('dwSignalNo', DWORD),
    ('dwCutTop', DWORD),
    ('dwCutBottom', DWORD),
    ('dwCutLeft', DWORD),
    ('dwCutRight', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_SIGNAL_CUTPARAM = struct_tagNET_DVR_SIGNAL_CUTPARAM
LPNET_DVR_SIGNAL_CUTPARAM = POINTER(struct_tagNET_DVR_SIGNAL_CUTPARAM)
tagNET_DVR_SIGNAL_CUTPARAM = struct_tagNET_DVR_SIGNAL_CUTPARAM
