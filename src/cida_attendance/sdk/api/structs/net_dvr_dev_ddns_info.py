from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEV_DDNS_INFO(Structure):
    pass

_S(struct_tagNET_DVR_DEV_DDNS_INFO, [
    ('byDevAddress', BYTE * 64),
    ('byTransProtocol', BYTE),
    ('byTransMode', BYTE),
    ('byDdnsType', BYTE),
    ('byRes1', BYTE),
    ('byDdnsAddress', BYTE * 64),
    ('wDdnsPort', WORD),
    ('byChanType', BYTE),
    ('byFactoryType', BYTE),
    ('dwChannel', DWORD),
    ('byStreamId', BYTE * 32),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('wDevPort', WORD),
    ('byRes2', BYTE * 2),
])

NET_DVR_DEV_DDNS_INFO = struct_tagNET_DVR_DEV_DDNS_INFO
LPNET_DVR_DEV_DDNS_INFO = POINTER(struct_tagNET_DVR_DEV_DDNS_INFO)
tagNET_DVR_DEV_DDNS_INFO = struct_tagNET_DVR_DEV_DDNS_INFO
