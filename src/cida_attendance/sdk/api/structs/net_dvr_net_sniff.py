from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_NET_SNIFF(Structure):
    pass

_S(struct_tagNET_DVR_NET_SNIFF, [
    ('byEnableSourcePort', BYTE),
    ('byEnableDestAddr', BYTE),
    ('byEnableDestPort', BYTE),
    ('byRes1', BYTE),
    ('bySourceIpAddr', BYTE * 64),
    ('byDestinationIpAddr', BYTE * 64),
    ('wSourcePort', WORD),
    ('wDestinationPort', WORD),
    ('byRes', BYTE * 16),
])

NET_DVR_NET_SNIFF = struct_tagNET_DVR_NET_SNIFF
LPNET_DVR_NET_SNIFF = POINTER(struct_tagNET_DVR_NET_SNIFF)
tagNET_DVR_NET_SNIFF = struct_tagNET_DVR_NET_SNIFF
