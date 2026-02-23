from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DDNS_STREAM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_DDNS_STREAM_CFG, [
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struStreamServer', NET_DVR_IPADDR),
    ('wStreamServerPort', WORD),
    ('byStreamServerTransmitType', BYTE),
    ('byRes2', BYTE),
    ('struIPServer', NET_DVR_IPADDR),
    ('wIPServerPort', WORD),
    ('byRes3', BYTE * 2),
    ('sDVRName', BYTE * 32),
    ('wDVRNameLen', WORD),
    ('wDVRSerialLen', WORD),
    ('sDVRSerialNumber', BYTE * 48),
    ('sUserName', BYTE * 32),
    ('sPassWord', BYTE * 16),
    ('wDVRPort', WORD),
    ('byRes4', BYTE * 2),
    ('byChannel', BYTE),
    ('byTransProtocol', BYTE),
    ('byTransMode', BYTE),
    ('byFactoryType', BYTE),
])

NET_DVR_DDNS_STREAM_CFG = struct_tagNET_DVR_DDNS_STREAM_CFG
LPNET_DVR_DDNS_STREAM_CFG = POINTER(struct_tagNET_DVR_DDNS_STREAM_CFG)
tagNET_DVR_DDNS_STREAM_CFG = struct_tagNET_DVR_DDNS_STREAM_CFG
