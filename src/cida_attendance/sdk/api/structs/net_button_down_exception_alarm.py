from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_BUTTON_DOWN_EXCEPTION_ALARM(Structure):
    pass

_S(struct_tagNET_BUTTON_DOWN_EXCEPTION_ALARM, [
    ('dwSize', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('byRes', BYTE * 64),
])

NET_BUTTON_DOWN_EXCEPTION_ALARM = struct_tagNET_BUTTON_DOWN_EXCEPTION_ALARM
LPNET_BUTTON_DOWN_EXCEPTION_ALARM = POINTER(struct_tagNET_BUTTON_DOWN_EXCEPTION_ALARM)
tagNET_BUTTON_DOWN_EXCEPTION_ALARM = struct_tagNET_BUTTON_DOWN_EXCEPTION_ALARM
