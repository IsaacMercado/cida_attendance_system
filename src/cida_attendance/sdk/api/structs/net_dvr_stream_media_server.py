from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STREAM_MEDIA_SERVER(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_MEDIA_SERVER, [
    ('byValid', BYTE),
    ('byRes1', BYTE * 3),
    ('byAddress', BYTE * 64),
    ('wDevPort', WORD),
    ('byTransmitType', BYTE),
    ('byRes2', BYTE * 5),
])

NET_DVR_STREAM_MEDIA_SERVER = struct_tagNET_DVR_STREAM_MEDIA_SERVER
LPNET_DVR_STREAM_MEDIA_SERVER = POINTER(struct_tagNET_DVR_STREAM_MEDIA_SERVER)
tagNET_DVR_STREAM_MEDIA_SERVER = struct_tagNET_DVR_STREAM_MEDIA_SERVER
