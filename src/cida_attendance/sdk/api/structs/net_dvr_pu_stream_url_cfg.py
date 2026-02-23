from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PU_STREAM_URL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PU_STREAM_URL_CFG, [
    ('byEnable', BYTE),
    ('byRes', BYTE * 3),
    ('byStreamMediaIP', BYTE * 64),
    ('wStreamMediaPort', WORD),
    ('byTransmitType', BYTE),
    ('byRes1', BYTE * 33),
    ('byDevIP', BYTE * 64),
    ('wDevPort', WORD),
    ('byChannel', BYTE),
    ('byTransMode', BYTE),
    ('byProType', BYTE),
    ('byTransProtocol', BYTE),
    ('byRes3', BYTE * 2),
    ('sUserName', BYTE * 32),
    ('sPassWord', BYTE * 16),
    ('byRes2', BYTE * 28),
])

NET_DVR_PU_STREAM_URL_CFG = struct_tagNET_DVR_PU_STREAM_URL_CFG
LPNET_DVR_PU_STREAM_URL_CFG = POINTER(struct_tagNET_DVR_PU_STREAM_URL_CFG)
tagNET_DVR_PU_STREAM_URL_CFG = struct_tagNET_DVR_PU_STREAM_URL_CFG
