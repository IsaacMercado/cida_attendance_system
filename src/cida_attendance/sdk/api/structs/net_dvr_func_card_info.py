from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_card_port_info import NET_DVR_CARD_PORT_INFO


class struct_tagNET_DVR_FUNC_CARD_INFO(Structure):
    pass

_S(struct_tagNET_DVR_FUNC_CARD_INFO, [
    ('dwCardNo', DWORD),
    ('byTypeName', BYTE * 32),
    ('bySerialNo', BYTE * 48),
    ('bySoftwareVersion', BYTE * 32),
    ('dwMainSlot', DWORD),
    ('byStructureType', BYTE),
    ('byRes1', BYTE * 3),
    ('struFuncPortInfo', NET_DVR_CARD_PORT_INFO * 4),
    ('byRes2', BYTE * 32),
])

NET_DVR_FUNC_CARD_INFO = struct_tagNET_DVR_FUNC_CARD_INFO
LPNET_DVR_FUNC_CARD_INFO = POINTER(struct_tagNET_DVR_FUNC_CARD_INFO)
tagNET_DVR_FUNC_CARD_INFO = struct_tagNET_DVR_FUNC_CARD_INFO
