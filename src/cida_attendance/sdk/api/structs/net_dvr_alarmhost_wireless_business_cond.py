from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_WIRELESS_BUSINESS_COND(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_WIRELESS_BUSINESS_COND, [
    ('dwSize', DWORD),
    ('byCommOperatorNum', BYTE * 32),
    ('byQueryCode', BYTE * 16),
    ('byBusinessType', BYTE),
    ('byRes', BYTE * 35),
])

NET_DVR_ALARMHOST_WIRELESS_BUSINESS_COND = struct_tagNET_DVR_ALARMHOST_WIRELESS_BUSINESS_COND
LPNET_DVR_ALARMHOST_WIRELESS_BUSINESS_COND = POINTER(struct_tagNET_DVR_ALARMHOST_WIRELESS_BUSINESS_COND)
tagNET_DVR_ALARMHOST_WIRELESS_BUSINESS_COND = struct_tagNET_DVR_ALARMHOST_WIRELESS_BUSINESS_COND
