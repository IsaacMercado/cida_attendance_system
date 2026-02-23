from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_ipaddr_union import NET_DVR_IPADDR_UNION


class struct_tagNET_DVR_LINK_ADDR(Structure):
    pass

_S(struct_tagNET_DVR_LINK_ADDR, [
    ('uLocalIP', NET_DVR_IPADDR_UNION),
    ('wLocalPort', WORD * 10),
    ('byLocalPortNum', BYTE),
    ('byRes1', BYTE * 3),
    ('uDevIP', NET_DVR_IPADDR_UNION),
    ('wDevPort', WORD * 10),
    ('byDevPortNum', BYTE),
    ('byRes2', BYTE * 3),
    ('byRes', BYTE * 80),
])

NET_DVR_LINK_ADDR = struct_tagNET_DVR_LINK_ADDR
LPNET_DVR_LINK_ADDR = POINTER(struct_tagNET_DVR_LINK_ADDR)
tagNET_DVR_LINK_ADDR = struct_tagNET_DVR_LINK_ADDR
