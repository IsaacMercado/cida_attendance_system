from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_145 import NET_DVR_JPEGPARA


class struct_tagNET_IVMS_ALARM_JPEG(Structure):
    pass

_S(struct_tagNET_IVMS_ALARM_JPEG, [
    ('byPicProType', BYTE),
    ('byRes', BYTE * 3),
    ('struPicParam', NET_DVR_JPEGPARA),
])

NET_IVMS_ALARM_JPEG = struct_tagNET_IVMS_ALARM_JPEG
LPNET_IVMS_ALARM_JPEG = POINTER(struct_tagNET_IVMS_ALARM_JPEG)
tagNET_IVMS_ALARM_JPEG = struct_tagNET_IVMS_ALARM_JPEG
