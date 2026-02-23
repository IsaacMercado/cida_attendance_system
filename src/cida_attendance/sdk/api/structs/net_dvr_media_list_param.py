from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MEDIA_LIST_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_MEDIA_LIST_PARAM, [
    ('byOperateCmd', BYTE),
    ('byRes', BYTE * 15),
])

NET_DVR_MEDIA_LIST_PARAM = struct_tagNET_DVR_MEDIA_LIST_PARAM
LPNET_DVR_MEDIA_LIST_PARAM = POINTER(struct_tagNET_DVR_MEDIA_LIST_PARAM)
tagNET_DVR_MEDIA_LIST_PARAM = struct_tagNET_DVR_MEDIA_LIST_PARAM
