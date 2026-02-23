from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SMSLISTINFO(Structure):
    pass

_S(struct_tagNET_DVR_SMSLISTINFO, [
    ('dwSize', DWORD),
    ('dwTotalSmsNum', DWORD),
    ('byRes', BYTE * 8),
    ('pSmsParam', POINTER(BYTE)),
    ('dwBufLen', DWORD),
])

NET_DVR_SMSLISTINFO = struct_tagNET_DVR_SMSLISTINFO
LPNET_DVR_SMSLISTINFO = POINTER(struct_tagNET_DVR_SMSLISTINFO)
tagNET_DVR_SMSLISTINFO = struct_tagNET_DVR_SMSLISTINFO
