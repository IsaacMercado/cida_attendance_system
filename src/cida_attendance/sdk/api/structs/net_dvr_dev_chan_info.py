from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DEV_CHAN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_DEV_CHAN_INFO, [
    ('struIP', NET_DVR_IPADDR),
    ('wDVRPort', WORD),
    ('byChannel', BYTE),
    ('byTransProtocol', BYTE),
    ('byTransMode', BYTE),
    ('byFactoryType', BYTE),
    ('byDeviceType', BYTE),
    ('byDispChan', BYTE),
    ('bySubDispChan', BYTE),
    ('byResolution', BYTE),
    ('byRes', BYTE * 2),
    ('byDomain', BYTE * 64),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
])

NET_DVR_DEV_CHAN_INFO = struct_tagNET_DVR_DEV_CHAN_INFO
LPNET_DVR_DEV_CHAN_INFO = POINTER(struct_tagNET_DVR_DEV_CHAN_INFO)
tagNET_DVR_DEV_CHAN_INFO = struct_tagNET_DVR_DEV_CHAN_INFO
