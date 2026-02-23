from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_phonecfg_v50 import NET_DVR_PHONECFG_V50


class struct_tagNET_DVR_SMSRELATIVEPARAM_V50(Structure):
    pass

_S(struct_tagNET_DVR_SMSRELATIVEPARAM_V50, [
    ('dwSize', DWORD),
    ('bEnableSmsAlarm', BYTE),
    ('byRes1', BYTE * 7),
    ('struAllowList', NET_DVR_PHONECFG_V50 * 32),
    ('byRes2', BYTE * 32),
])

NET_DVR_SMSRELATIVEPARAM_V50 = struct_tagNET_DVR_SMSRELATIVEPARAM_V50
LPNET_DVR_SMSRELATIVEPARAM_V50 = POINTER(struct_tagNET_DVR_SMSRELATIVEPARAM_V50)
tagNET_DVR_SMSRELATIVEPARAM_V50 = struct_tagNET_DVR_SMSRELATIVEPARAM_V50
