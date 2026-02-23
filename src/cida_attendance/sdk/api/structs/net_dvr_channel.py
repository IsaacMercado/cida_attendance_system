from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CHANNEL(Structure):
    pass

_S(struct_tagNET_DVR_CHANNEL, [
    ('byAddress', BYTE * 64),
    ('wDVRPort', WORD),
    ('byRes1', BYTE * 2),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('dwChannel', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_CHANNEL = struct_tagNET_DVR_CHANNEL
LPNET_DVR_CHANNEL = POINTER(struct_tagNET_DVR_CHANNEL)
tagNET_DVR_CHANNEL = struct_tagNET_DVR_CHANNEL
