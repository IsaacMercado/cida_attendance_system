from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNet_DVR_DDNS_ADDRESS(Structure):
    pass

_S(struct_tagNet_DVR_DDNS_ADDRESS, [
    ('byDevAddress', BYTE * 64),
    ('byDevDdns', BYTE * 64),
    ('byDdnsType', BYTE),
    ('byRes1', BYTE * 3),
    ('wDevPort', WORD),
    ('wDdnsPort', WORD),
    ('byres', BYTE * 64),
])

NET_DVR_DDNS_ADDRESS = struct_tagNet_DVR_DDNS_ADDRESS
LPNET_DVR_DDNS_ADDRESS = POINTER(struct_tagNet_DVR_DDNS_ADDRESS)
tagNet_DVR_DDNS_ADDRESS = struct_tagNet_DVR_DDNS_ADDRESS
