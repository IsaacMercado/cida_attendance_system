from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .anon_224 import NET_DVR_VCA_ATTEND_PICDATA


class struct_anon_225(Structure):
    pass

_S(struct_anon_225, [
    ('byPicNum', BYTE),
    ('byRes1', BYTE * 3),
    ('struPicData', NET_DVR_VCA_ATTEND_PICDATA * 3),
    ('dwVideoLen', DWORD),
    ('pVideoBuf', String),
    ('byRes', BYTE * 64),
])

NET_DVR_VCA_ATTEND_PICTURE_INFO = struct_anon_225
LPNET_DVR_VCA_ATTEND_PICTURE_INFO = POINTER(struct_anon_225)
