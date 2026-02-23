from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STREAM_URL_V40(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_URL_V40, [
    ('byEnable', BYTE),
    ('byStreamType', BYTE),
    ('byLocalBackUp', BYTE),
    ('byRes', BYTE),
    ('strURL', BYTE * 256),
    ('dwProtocalType', DWORD),
    ('sUserName', BYTE * 32),
    ('sPassWord', BYTE * 16),
    ('byAddress', BYTE * 64),
    ('wIPPort', WORD),
    ('wChanNo', WORD),
    ('byVAGChanNo', BYTE * 32),
    ('byRes1', BYTE * 88),
])

NET_DVR_STREAM_URL_V40 = struct_tagNET_DVR_STREAM_URL_V40
LPNET_DVR_STREAM_URL_V40 = POINTER(struct_tagNET_DVR_STREAM_URL_V40)
tagNET_DVR_STREAM_URL_V40 = struct_tagNET_DVR_STREAM_URL_V40
