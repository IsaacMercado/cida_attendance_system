from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_MANAGE_UNIT_RELATEDEV(Structure):
    pass

_S(struct_tagNET_DVR_MANAGE_UNIT_RELATEDEV, [
    ('struSIPServer', NET_DVR_IPADDR),
    ('byRes', BYTE * 880),
])

NET_DVR_MANAGE_UNIT_RELATEDEV = struct_tagNET_DVR_MANAGE_UNIT_RELATEDEV
LPNET_DVR_MANAGE_UNIT_RELATEDEV = POINTER(struct_tagNET_DVR_MANAGE_UNIT_RELATEDEV)
tagNET_DVR_MANAGE_UNIT_RELATEDEV = struct_tagNET_DVR_MANAGE_UNIT_RELATEDEV
