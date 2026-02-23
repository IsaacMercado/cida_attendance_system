from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_card_port_info import NET_DVR_CARD_PORT_INFO


class struct_tagNET_DVR_NETMGR_CARD_INFO_V50(Structure):
    pass

_S(struct_tagNET_DVR_NETMGR_CARD_INFO_V50, [
    ('byMainSlotNo', BYTE),
    ('byRes1', BYTE * 3),
    ('byTypeName', BYTE * 32),
    ('bySerialNo', BYTE * 48),
    ('bySoftwareVersion', BYTE * 32),
    ('byHardwareVersion', BYTE * 32),
    ('struIPAddr', NET_DVR_IPADDR),
    ('struMask', NET_DVR_IPADDR),
    ('struGateway', NET_DVR_IPADDR),
    ('byMacAddr', BYTE * 6),
    ('bySlotNums', BYTE),
    ('byStructureType', BYTE),
    ('struPortInfo', NET_DVR_CARD_PORT_INFO * 4),
    ('byRes2', BYTE * 64),
])

NET_DVR_NETMGR_CARD_INFO_V50 = struct_tagNET_DVR_NETMGR_CARD_INFO_V50
LPNET_DVR_NETMGR_CARD_INFO_V50 = POINTER(struct_tagNET_DVR_NETMGR_CARD_INFO_V50)
tagNET_DVR_NETMGR_CARD_INFO_V50 = struct_tagNET_DVR_NETMGR_CARD_INFO_V50
