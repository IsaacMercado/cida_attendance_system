from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_phonecfg import NET_DVR_PHONECFG


class struct_tagNET_DVR_SMSRELATIVEPARAM(Structure):
    pass

_S(struct_tagNET_DVR_SMSRELATIVEPARAM, [
    ('dwSize', DWORD),
    ('bEnableSmsAlarm', BYTE),
    ('byRes1', BYTE * 7),
    ('struAllowList', NET_DVR_PHONECFG * 8),
    ('byRes2', BYTE * 32),
])

NET_DVR_SMSRELATIVEPARAM = struct_tagNET_DVR_SMSRELATIVEPARAM
LPNET_DVR_SMSRELATIVEPARAM = POINTER(struct_tagNET_DVR_SMSRELATIVEPARAM)
tagNET_DVR_SMSRELATIVEPARAM = struct_tagNET_DVR_SMSRELATIVEPARAM
