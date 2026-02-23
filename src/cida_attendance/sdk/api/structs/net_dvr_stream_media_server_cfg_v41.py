from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STREAM_MEDIA_SERVER_CFG_V41(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_MEDIA_SERVER_CFG_V41, [
    ('byValid', BYTE),
    ('byRes1', BYTE * 3),
    ('byAddress', BYTE * 64),
    ('wDevPort', WORD),
    ('byTransmitType', BYTE),
    ('byRes2', BYTE * 69),
])

NET_DVR_STREAM_MEDIA_SERVER_CFG_V41 = struct_tagNET_DVR_STREAM_MEDIA_SERVER_CFG_V41
LPNET_DVR_STREAM_MEDIA_SERVER_CFG_V41 = POINTER(struct_tagNET_DVR_STREAM_MEDIA_SERVER_CFG_V41)
tagNET_DVR_STREAM_MEDIA_SERVER_CFG_V41 = struct_tagNET_DVR_STREAM_MEDIA_SERVER_CFG_V41
