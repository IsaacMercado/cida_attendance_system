from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEV_CHAN_INFO_EX(Structure):
    pass

_S(struct_tagNET_DVR_DEV_CHAN_INFO_EX, [
    ('byChanType', BYTE),
    ('byStreamId', BYTE * 32),
    ('byRes1', BYTE * 3),
    ('dwChannel', DWORD),
    ('byRes2', BYTE * 24),
    ('byAddress', BYTE * 64),
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
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
])

NET_DVR_DEV_CHAN_INFO_EX = struct_tagNET_DVR_DEV_CHAN_INFO_EX
LPNET_DVR_DEV_CHAN_INFO_EX = POINTER(struct_tagNET_DVR_DEV_CHAN_INFO_EX)
tagNET_DVR_DEV_CHAN_INFO_EX = struct_tagNET_DVR_DEV_CHAN_INFO_EX
