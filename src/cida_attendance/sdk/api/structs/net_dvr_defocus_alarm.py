from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_DEFOCUS_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_DEFOCUS_ALARM, [
    ('dwSize', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('wDevInfoIvmsChannelEx', WORD),
    ('byRes1', BYTE * 2),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('byTimeDiffFlag', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('byRes', BYTE * 49),
])

NET_DVR_DEFOCUS_ALARM = struct_tagNET_DVR_DEFOCUS_ALARM
LPNET_DVR_DEFOCUS_ALARM = POINTER(struct_tagNET_DVR_DEFOCUS_ALARM)
tagNET_DVR_DEFOCUS_ALARM = struct_tagNET_DVR_DEFOCUS_ALARM
