from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_NAT_PORT(Structure):
    pass

_S(struct_tagNET_DVR_NAT_PORT, [
    ('wEnable', WORD),
    ('wExtPort', WORD),
    ('byRes', BYTE * 12),
])

NET_DVR_NAT_PORT = struct_tagNET_DVR_NAT_PORT
LPNET_DVR_NAT_PORT = POINTER(struct_tagNET_DVR_NAT_PORT)
tagNET_DVR_NAT_PORT = struct_tagNET_DVR_NAT_PORT
