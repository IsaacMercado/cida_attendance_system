from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ASSOCIATEDDEV_CHAN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ASSOCIATEDDEV_CHAN_INFO, [
    ('dwSize', DWORD),
    ('sAddress', BYTE * 64),
    ('wDVRPort', WORD),
    ('wChannel', WORD),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byRes', BYTE * 24),
])

NET_DVR_ASSOCIATEDDEV_CHAN_INFO = struct_tagNET_DVR_ASSOCIATEDDEV_CHAN_INFO
LPNET_DVR_ASSOCIATEDDEV_CHAN_INFO = POINTER(struct_tagNET_DVR_ASSOCIATEDDEV_CHAN_INFO)
tagNET_DVR_ASSOCIATEDDEV_CHAN_INFO = struct_tagNET_DVR_ASSOCIATEDDEV_CHAN_INFO
