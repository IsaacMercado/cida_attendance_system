from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_I_FRAME(Structure):
    pass

_S(struct_tagNET_DVR_I_FRAME, [
    ('dwSize', DWORD),
    ('sStreamID', BYTE * 32),
    ('dwChan', DWORD),
    ('byStreamType', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_I_FRAME = struct_tagNET_DVR_I_FRAME
LPNET_DVR_I_FRAME = POINTER(struct_tagNET_DVR_I_FRAME)
tagNET_DVR_I_FRAME = struct_tagNET_DVR_I_FRAME
