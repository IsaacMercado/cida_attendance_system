from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_STREAM_CALLBACK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_STREAM_CALLBACK_CFG, [
    ('byPlayBackEndFlag', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_LOCAL_STREAM_CALLBACK_CFG = struct_tagNET_DVR_LOCAL_STREAM_CALLBACK_CFG
LPNET_DVR_LOCAL_STREAM_CALLBACK_CFG = POINTER(struct_tagNET_DVR_LOCAL_STREAM_CALLBACK_CFG)
tagNET_DVR_LOCAL_STREAM_CALLBACK_CFG = struct_tagNET_DVR_LOCAL_STREAM_CALLBACK_CFG
