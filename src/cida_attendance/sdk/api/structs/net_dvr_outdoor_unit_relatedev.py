from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_OUTDOOR_UNIT_RELATEDEV(Structure):
    pass

_S(struct_tagNET_DVR_OUTDOOR_UNIT_RELATEDEV, [
    ('struMainOutdoorUnit', NET_DVR_IPADDR),
    ('struManageUnit', NET_DVR_IPADDR),
    ('struSIPServer', NET_DVR_IPADDR),
    ('byManageCenterID', BYTE * 32),
    ('byRes', BYTE * 560),
])

NET_DVR_OUTDOOR_UNIT_RELATEDEV = struct_tagNET_DVR_OUTDOOR_UNIT_RELATEDEV
LPNET_DVR_OUTDOOR_UNIT_RELATEDEV = POINTER(struct_tagNET_DVR_OUTDOOR_UNIT_RELATEDEV)
tagNET_DVR_OUTDOOR_UNIT_RELATEDEV = struct_tagNET_DVR_OUTDOOR_UNIT_RELATEDEV
