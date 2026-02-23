from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_145 import NET_DVR_JPEGPARA


class struct_anon_146(Structure):
    pass

_S(struct_anon_146, [
    ('struParam', NET_DVR_JPEGPARA),
    ('byPicFormat', BYTE),
    ('byCapturePicType', BYTE),
    ('bySceneID', BYTE),
    ('byRes', BYTE * 253),
])

NET_DVR_PICPARAM_V50 = struct_anon_146
LPNET_DVR_PICPARAM_V50 = POINTER(struct_anon_146)
