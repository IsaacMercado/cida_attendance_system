from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_tagNET_DVR_DOWN_LOAD_REQUEST(Structure):
    pass

_S(struct_tagNET_DVR_DOWN_LOAD_REQUEST, [
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('sSnapShotURL', c_char * 256),
    ('byRes', BYTE * 32),
])

NET_DVR_DOWN_LOAD_REQUEST = struct_tagNET_DVR_DOWN_LOAD_REQUEST
LPNET_DVR_DOWN_LOAD_REQUEST = POINTER(struct_tagNET_DVR_DOWN_LOAD_REQUEST)
tagNET_DVR_DOWN_LOAD_REQUEST = struct_tagNET_DVR_DOWN_LOAD_REQUEST
