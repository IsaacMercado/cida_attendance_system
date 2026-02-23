from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_AGAIN_RELATEDEV(Structure):
    pass

_S(struct_tagNET_DVR_AGAIN_RELATEDEV, [
    ('struSIPServer', NET_DVR_IPADDR),
    ('struCenterAddr', NET_DVR_IPADDR),
    ('wCenterPort', WORD),
    ('byRes1', BYTE * 2),
    ('struIndoorUnit', NET_DVR_IPADDR),
    ('struAgainAddr', NET_DVR_IPADDR),
    ('byRes', BYTE * 444),
])

NET_DVR_AGAIN_RELATEDEV = struct_tagNET_DVR_AGAIN_RELATEDEV
LPNET_DVR_AGAIN_RELATEDEV = POINTER(struct_tagNET_DVR_AGAIN_RELATEDEV)
tagNET_DVR_AGAIN_RELATEDEV = struct_tagNET_DVR_AGAIN_RELATEDEV
