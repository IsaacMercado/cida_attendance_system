from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ANR_ARMING_HOST(Structure):
    pass

_S(struct_tagNET_DVR_ANR_ARMING_HOST, [
    ('dwSize', DWORD),
    ('struANRArmingHostIpAddr', NET_DVR_IPADDR),
    ('wANRAlarmHostPort', WORD),
    ('byANRAlarmType', BYTE),
    ('byConfirmMechanismEnabled', BYTE),
    ('byRes', BYTE * 512),
])

NET_DVR_ANR_ARMING_HOST = struct_tagNET_DVR_ANR_ARMING_HOST
LPNET_DVR_ANR_ARMING_HOST = POINTER(struct_tagNET_DVR_ANR_ARMING_HOST)
tagNET_DVR_ANR_ARMING_HOST = struct_tagNET_DVR_ANR_ARMING_HOST
