from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ADDR_DOMAIN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ADDR_DOMAIN_INFO, [
    ('szDomainAddr', BYTE * 64),
    ('wPort', WORD),
    ('byRes', BYTE * 2),
])

NET_DVR_ADDR_DOMAIN_INFO = struct_tagNET_DVR_ADDR_DOMAIN_INFO
LPNET_DVR_ADDR_DOMAIN_INFO = POINTER(struct_tagNET_DVR_ADDR_DOMAIN_INFO)
tagNET_DVR_ADDR_DOMAIN_INFO = struct_tagNET_DVR_ADDR_DOMAIN_INFO
