from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_REMOTE_PLAY_(Structure):
    pass

_S(struct__NET_DVR_REMOTE_PLAY_, [
    ('dwSize', DWORD),
    ('byFileName', BYTE * 32),
    ('byVideoOut', BYTE * 7),
    ('byRes1', BYTE * 5),
    ('byType', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_REMOTE_PLAY = struct__NET_DVR_REMOTE_PLAY_
LPNET_DVR_REMOTE_PLAY = POINTER(struct__NET_DVR_REMOTE_PLAY_)
_NET_DVR_REMOTE_PLAY_ = struct__NET_DVR_REMOTE_PLAY_
