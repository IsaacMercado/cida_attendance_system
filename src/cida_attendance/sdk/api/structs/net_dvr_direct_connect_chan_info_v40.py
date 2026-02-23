from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DIRECT_CONNECT_CHAN_INFO_V40(Structure):
    pass

_S(struct_tagNET_DVR_DIRECT_CONNECT_CHAN_INFO_V40, [
    ('byEnable', BYTE),
    ('byProType', BYTE),
    ('byZeroChan', BYTE),
    ('byRes1', BYTE),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byAddress', BYTE * 64),
    ('wDVRPort', WORD),
    ('byStreamType', BYTE),
    ('byOnline', BYTE),
    ('dwChannel', DWORD),
    ('byTransProtocol', BYTE),
    ('byLocalBackUp', BYTE),
    ('byRes3', BYTE * 2),
    ('byVAGChanNo', BYTE * 32),
    ('byRes', BYTE * 340),
])

NET_DVR_DIRECT_CONNECT_CHAN_INFO_V40 = struct_tagNET_DVR_DIRECT_CONNECT_CHAN_INFO_V40
LPNET_DVR_DIRECT_CONNECT_CHAN_INFO_V40 = POINTER(struct_tagNET_DVR_DIRECT_CONNECT_CHAN_INFO_V40)
tagNET_DVR_DIRECT_CONNECT_CHAN_INFO_V40 = struct_tagNET_DVR_DIRECT_CONNECT_CHAN_INFO_V40
