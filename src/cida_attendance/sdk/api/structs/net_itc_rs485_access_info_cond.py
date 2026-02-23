from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_RS485_ACCESS_INFO_COND(Structure):
    pass

_S(struct_tagNET_ITC_RS485_ACCESS_INFO_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwTriggerModeType', DWORD),
    ('byAssociateRS485No', BYTE),
    ('byRes', BYTE * 15),
])

NET_ITC_RS485_ACCESS_INFO_COND = struct_tagNET_ITC_RS485_ACCESS_INFO_COND
LPNET_ITC_RS485_ACCESS_INFO_COND = POINTER(struct_tagNET_ITC_RS485_ACCESS_INFO_COND)
tagNET_ITC_RS485_ACCESS_INFO_COND = struct_tagNET_ITC_RS485_ACCESS_INFO_COND
