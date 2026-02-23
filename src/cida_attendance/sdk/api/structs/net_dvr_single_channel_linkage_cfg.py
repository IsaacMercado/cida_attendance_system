from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_446 import union_anon_446


class struct_tagNET_DVR_SINGLE_CHANNEL_LINKAGE_CFG_(Structure):
    pass

_S(struct_tagNET_DVR_SINGLE_CHANNEL_LINKAGE_CFG_, [
    ('byDDNSType', BYTE),
    ('byRes1', BYTE),
    ('wDDNSPort', WORD),
    ('byServerAddr', BYTE * 64),
    ('byDevName', BYTE * 64),
    ('byDevSerialNum', BYTE * 48),
    ('byAddressType', BYTE),
    ('byRes2', BYTE),
    ('wDevPort', WORD),
    ('unionDevAddr', union_anon_446),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('dwChannel', DWORD),
    ('byRes3', BYTE * 32),
])

NET_DVR_SINGLE_CHANNEL_LINKAGE_CFG = struct_tagNET_DVR_SINGLE_CHANNEL_LINKAGE_CFG_
LPNET_DVR_SINGLE_CHANNEL_LINKAGE_CFG = POINTER(struct_tagNET_DVR_SINGLE_CHANNEL_LINKAGE_CFG_)
tagNET_DVR_SINGLE_CHANNEL_LINKAGE_CFG_ = struct_tagNET_DVR_SINGLE_CHANNEL_LINKAGE_CFG_
