from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEV_CHAN_INFO_V41(Structure):
    pass

_S(struct_tagNET_DVR_DEV_CHAN_INFO_V41, [
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

NET_DVR_DEV_CHAN_INFO_V41 = struct_tagNET_DVR_DEV_CHAN_INFO_V41
LPNET_DVR_DEV_CHAN_INFO_V41 = POINTER(struct_tagNET_DVR_DEV_CHAN_INFO_V41)
tagNET_DVR_DEV_CHAN_INFO_V41 = struct_tagNET_DVR_DEV_CHAN_INFO_V41
