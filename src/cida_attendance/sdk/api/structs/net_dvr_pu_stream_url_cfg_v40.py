from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PU_STREAM_URL_CFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_PU_STREAM_URL_CFG_V40, [
    ('byEnable', BYTE),
    ('byRes', BYTE * 3),
    ('byStreamMediaIP', BYTE * 64),
    ('wStreamMediaPort', WORD),
    ('byTransmitType', BYTE),
    ('byRes1', BYTE),
    ('byDevIP', BYTE * 64),
    ('wDevPort', WORD),
    ('byChannel', BYTE),
    ('byTransMode', BYTE),
    ('byProType', BYTE),
    ('byTransProtocol', BYTE),
    ('byRes3', BYTE * 2),
    ('sUserName', BYTE * 32),
    ('sPassWord', BYTE * 16),
    ('byRes2', BYTE * 308),
])

NET_DVR_PU_STREAM_URL_CFG_V40 = struct_tagNET_DVR_PU_STREAM_URL_CFG_V40
LPNET_DVR_PU_STREAM_URL_CFG_V40 = POINTER(struct_tagNET_DVR_PU_STREAM_URL_CFG_V40)
tagNET_DVR_PU_STREAM_URL_CFG_V40 = struct_tagNET_DVR_PU_STREAM_URL_CFG_V40
