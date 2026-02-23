from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_INDOOR_UNIT_RELATEDEV(Structure):
    pass

_S(struct_tagNET_DVR_INDOOR_UNIT_RELATEDEV, [
    ('struOutdoorUnit', NET_DVR_IPADDR),
    ('struManageUnit', NET_DVR_IPADDR),
    ('struSIPServer', NET_DVR_IPADDR),
    ('struAgainUnit', NET_DVR_IPADDR),
    ('byOutDoorType', BYTE),
    ('byOutInConnectMode', BYTE),
    ('byIndoorConnectMode', BYTE),
    ('byRes1', BYTE),
    ('struIndoorUnit', NET_DVR_IPADDR),
    ('byManageCenterID', BYTE * 32),
    ('byRes', BYTE * 268),
])

NET_DVR_INDOOR_UNIT_RELATEDEV = struct_tagNET_DVR_INDOOR_UNIT_RELATEDEV
LPNET_DVR_INDOOR_UNIT_RELATEDEV = POINTER(struct_tagNET_DVR_INDOOR_UNIT_RELATEDEV)
tagNET_DVR_INDOOR_UNIT_RELATEDEV = struct_tagNET_DVR_INDOOR_UNIT_RELATEDEV
